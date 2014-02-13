#
# V-Ray For Blender
#
# http://chaosgroup.com
#
# Author: Andrei Izrantcev
# E-Mail: andrei.izrantcev@chaosgroup.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.
#

import bpy
import mathutils

import _vray_for_blender

from vb30.lib     import ExportUtils
from vb30.lib     import utils as LibUtils
from vb30.plugins import PLUGINS
from vb30.debug   import Debug, PrintDict
from vb30.utils   import get_name, clean_string, get_data_by_name


##     ## ######## #### ##       #### ######## #### ########  ######
##     ##    ##     ##  ##        ##     ##     ##  ##       ##    ##
##     ##    ##     ##  ##        ##     ##     ##  ##       ##
##     ##    ##     ##  ##        ##     ##     ##  ######    ######
##     ##    ##     ##  ##        ##     ##     ##  ##             ##
##     ##    ##     ##  ##        ##     ##     ##  ##       ##    ##
 #######     ##    #### ######## ####    ##    #### ########  ######

def GetNodeName(ntree, node):
    return clean_string("NT%sN%s" % (ntree.name, node.name))


def GetConnectedNode(ntree, nodeSocket):
    for l in nodeSocket.links:
        if l.from_node:
            return l.from_node
    return None


def GetConnectedSocket(ntree, nodeSocket):
    for l in nodeSocket.links:
        if l.from_socket:
            return l.from_socket
    return None


def GetNodesByType(ntree, nodeType):
    for n in ntree.nodes:
        if n.bl_idname == nodeType:
            yield n


def GetNodeByType(ntree, nodeType):
    if not ntree:
        return None
    for n in ntree.nodes:
        if n.bl_idname == nodeType:
            return n
    return None


def GetOutputNode(ntree):
    return GetNodeByType(ntree, 'VRayNodeOutputMaterial')


def GetOutputName(ntree):
    outputNode = GetNodeByType(ntree, 'VRayNodeOutputMaterial')
    if not outputNode:
        return None

    materialSocket = outputNode.inputs['Material']
    if not materialSocket.is_linked:
        return None

    connectedNode = GetConnectedNode(ntree, materialSocket)
    if not connectedNode:
        return None

    return GetNodeName(ntree, connectedNode)


 ######  ######## ##       ########  ######  ########  #######  ########   ######  
##    ## ##       ##       ##       ##    ##    ##    ##     ## ##     ## ##    ## 
##       ##       ##       ##       ##          ##    ##     ## ##     ## ##       
 ######  ######   ##       ######   ##          ##    ##     ## ########   ######  
      ## ##       ##       ##       ##          ##    ##     ## ##   ##         ## 
##    ## ##       ##       ##       ##    ##    ##    ##     ## ##    ##  ##    ## 
 ######  ######## ######## ########  ######     ##     #######  ##     ##  ######  

def WriteVRayNodeSelectObject(bus, nodetree, node):
    scene = bus['scene']
    if not node.objectName:
        return []
    if node.objectName not in scene.objects:
        return []
    return [scene.objects[node.objectName]]


def WriteVRayNodeSelectGroup(bus, nodetree, node):
    if not node.groupName:
        return []
    if node.groupName not in bpy.data.groups:
        return []
    return bpy.data.groups[node.groupName].objects


########  ##       ######## ##    ## ########  ######## ########      #######  ########        ## ########  ######  ######## 
##     ## ##       ##       ###   ## ##     ## ##       ##     ##    ##     ## ##     ##       ## ##       ##    ##    ##    
##     ## ##       ##       ####  ## ##     ## ##       ##     ##    ##     ## ##     ##       ## ##       ##          ##    
########  ##       ######   ## ## ## ##     ## ######   ########     ##     ## ########        ## ######   ##          ##    
##     ## ##       ##       ##  #### ##     ## ##       ##   ##      ##     ## ##     ## ##    ## ##       ##          ##    
##     ## ##       ##       ##   ### ##     ## ##       ##    ##     ##     ## ##     ## ##    ## ##       ##    ##    ##    
########  ######## ######## ##    ## ########  ######## ##     ##     #######  ########   ######  ########  ######     ##    

def WriteVRayNodeBlenderOutputGeometry(bus, nodetree, node):
    scene = bus['scene']
    ob    = bus['node']['object']
    o     = bus['output']

    VRayScene    = scene.vray
    VRayExporter = VRayScene.Exporter

    meshName = bus['node']['geometry']

    # XXX: Resolve manual meshes export
    #
    if not VRayExporter.auto_meshes:
        return meshName

    if meshName not in bus['cache']['mesh']:
        bus['cache']['mesh'].add(meshName)

        propGroup = node.GeomStaticMesh if node else ob.data.vray.GeomStaticMesh
        dynamic_geometry = propGroup.dynamic_geometry

        if bus['engine'] == 'VRAY_RENDER_RT' and VRayScene.RTEngine.use_opencl == '4':
            setattr(propGroup, 'dynamic_geometry', True)

        _vray_for_blender.exportMesh(
            bpy.context.as_pointer(),   # Context
            ob.as_pointer(),            # Object
            meshName,                   # Result plugin name
            propGroup,                  # PropertyGroup
            o.getFileByType('GEOMETRY') # Output file
        )

        if bus['engine'] == 'VRAY_RENDER_RT' and VRayScene.RTEngine.use_opencl == '4':
            setattr(propGroup, 'dynamic_geometry', dynamic_geometry)

    return meshName


def WriteVRayNodeBlenderOutputMaterial(bus, nodetree, node):
    scene = bus['scene']
    ob    = bus['node']['object']
    o     = bus['output']

    if not len(ob.material_slots):
        bus['node']['material'] = bus['defaults']['material']
        return bus['node']['material']

    VRayScene = scene.vray

    VRayExporter    = VRayScene.Exporter
    SettingsOptions = VRayScene.SettingsOptions

    # Multi-material name
    mtl_name = LibUtils.GetObjectName(ob, prefix='OBMA')

    # Collecting and exporting object materials
    mtls_list = []
    ids_list  = []
    ma_id     = 0

    for slot in ob.material_slots:
        if not slot.material:
            continue

        ma = slot.material

        if not ma.vray.ntree:
            continue

        nodeMaterial = WriteVRayMaterialNodeTree(bus, ma.vray.ntree)

        ma_id += 1
        mtls_list.append(nodeMaterial)
        ids_list.append(str(ma_id))

    # No materials assigned - use default material
    if len(mtls_list) == 0:
        bus['node']['material'] = bus['defaults']['material']

    # Only one material - no need for Multi-material
    elif len(mtls_list) == 1:
        bus['node']['material'] = mtls_list[0]

    # Several materials assigned - use Mutli-material
    else:
        bus['node']['material'] = mtl_name

        o.set('MATERIAL', 'MtlMulti', mtl_name)
        o.writeHeader()
        o.writeAttibute('mtls_list', "List(%s)" % ','.join(mtls_list))
        o.writeAttibute('ids_list', "ListInt(%s)" % ','.join(ids_list))
        o.writeFooter()

    return bus['node']['material']


##          ###    ##    ## ######## ########  ######## ########
##         ## ##    ##  ##  ##       ##     ## ##       ##     ##
##        ##   ##    ####   ##       ##     ## ##       ##     ##
##       ##     ##    ##    ######   ########  ######   ##     ##
##       #########    ##    ##       ##   ##   ##       ##     ##
##       ##     ##    ##    ##       ##    ##  ##       ##     ##
######## ##     ##    ##    ######## ##     ## ######## ########

def WriteVRayNodeTexLayered(bus, nodetree, node):
    scene = bus['scene']
    o     = bus['output']

    pluginName = clean_string("nt%sn%s" % (nodetree.name, node.name))

    textures    = []
    blend_modes = []
    
    for inputSocket in node.inputs:
        if not inputSocket.is_linked:
            continue

        textures.append(WriteConnectedNode(bus, nodetree, inputSocket))
        blend_modes.append(inputSocket.value)

    o.set('TEXTURE', 'TexLayered', pluginName)
    o.writeHeader()
    o.writeAttibute('textures', "List(%s)" % ','.join(reversed(textures)))
    o.writeAttibute('blend_modes', "List(%s)" % ','.join(reversed(blend_modes)))
    o.writeFooter()

    return pluginName


def WriteVRayNodeBRDFLayered(bus, nodetree, node):
    scene = bus['scene']
    o     = bus['output']

    pluginName = clean_string("nt%sn%s" % (nodetree.name, node.name))

    brdfs   = []
    weights = []

    for i in range(int(len(node.inputs) / 2)):
        layer = i+1
        brdfSocket   = "BRDF %i"   % layer
        weightSocket = "Weight %i" % layer

        if not node.inputs[brdfSocket].is_linked:
            continue

        brdfs.append(WriteConnectedNode(bus, nodetree, node.inputs[brdfSocket]))

        if node.inputs[weightSocket].is_linked:
            weigthNode = GetConnectedNode(nodetree, node.inputs[weightSocket])
            weights.append(WriteNode(bus, nodetree, weigthNode))
        else:
            weightParam = "%sW%sI%i"%(pluginName, brdfs[i], i)
            
            weightColor = mathutils.Color([node.inputs[weightSocket].value]*3)

            o.set('TEXTURE', 'TexAColor', weightParam)
            o.writeHeader()
            o.writeAttibute('texture', LibUtils.AnimatedValue(scene, weightColor))
            o.writeFooter()
            
            weights.append(weightParam)

    o.set('BRDF', 'BRDFLayered', pluginName)
    o.writeHeader()
    o.writeAttibute('brdfs', "List(%s)" % ','.join(brdfs))
    o.writeAttibute('weights', "List(%s)" % ','.join(weights))
    o.writeAttibute('additive_mode', LibUtils.FormatValue(node.additive_mode))
    o.writeFooter()

    return pluginName


######## ##     ## ########   #######  ########  ########
##        ##   ##  ##     ## ##     ## ##     ##    ##
##         ## ##   ##     ## ##     ## ##     ##    ##
######      ###    ########  ##     ## ########     ##
##         ## ##   ##        ##     ## ##   ##      ##
##        ##   ##  ##        ##     ## ##    ##     ##
######## ##     ## ##         #######  ##     ##    ##

def WriteConnectedNode(bus, nodetree, nodeSocket, returnDefault=True):
    Debug("Processing socket: %s [%s]" % (nodeSocket.name, nodeSocket.vray_attr))

    if not nodeSocket.is_linked:
        if returnDefault:
            return nodeSocket.value
        else:
            return None
    
    connectedNode   = GetConnectedNode(nodetree, nodeSocket)
    connectedSocket = GetConnectedSocket(nodetree, nodeSocket)
    if connectedNode:
        vrayPlugin = WriteNode(bus, nodetree, connectedNode, returnDefault=returnDefault)

        if connectedSocket.vray_attr and connectedSocket.vray_attr not in {'NONE'}:
            # XXX: use as a workaround
            # TODO: get plugin desc and check if the attr is output,
            # but skip uvwgen anyway.
            #
            if connectedSocket.vray_attr not in {'uvwgen', 'bitmap'}:
                vrayPlugin = "%s::%s" % (vrayPlugin, connectedSocket.vray_attr)

                if connectedNode.bl_idname == 'VRayNodeTexMayaFluid':
                    vrayPlugin = vrayPlugin.replace("::out_flame",   "@Flame")
                    vrayPlugin = vrayPlugin.replace("::out_density", "@Density")
                    vrayPlugin = vrayPlugin.replace("::out_fuel",    "@Fuel")

        return vrayPlugin
    
    return None


def WriteNode(bus, nodetree, node, returnDefault=False):
    Debug("Processing node: %s..." % node.name)

    # Write some nodes in a special way
    if node.bl_idname == 'VRayNodeBRDFLayered':
        return WriteVRayNodeBRDFLayered(bus, nodetree, node)
    elif node.bl_idname == 'VRayNodeTexLayered':
        return WriteVRayNodeTexLayered(bus, nodetree, node)
    elif node.bl_idname == 'VRayNodeSelectObject':
        return WriteVRayNodeSelectObject(bus, nodetree, node)
    elif node.bl_idname == 'VRayNodeSelectGroup':
        return WriteVRayNodeSelectGroup(bus, nodetree, node)
    elif node.bl_idname == 'VRayNodeBlenderOutputGeometry':
        return WriteVRayNodeBlenderOutputGeometry(bus, nodetree, node)
    elif node.bl_idname == 'VRayNodeBlenderOutputMaterial':
        return WriteVRayNodeBlenderOutputMaterial(bus, nodetree, node)

    pluginName = clean_string("NT%sN%s" % (nodetree.name, node.name))
    if pluginName in bus['cache']['plugins']:
        return pluginName
    bus['cache']['plugins'].add(pluginName)

    vrayType   = node.vray_type
    vrayPlugin = node.vray_plugin

    if vrayType == 'NONE' or vrayPlugin == 'NONE':
        return None

    Debug("Generating plugin \"%s\" [%s, %s]" % (pluginName, vrayType, vrayPlugin), msgType='INFO')

    propGroup = getattr(node, vrayPlugin)

    socketParams = {}

    for nodeSocket in node.inputs:
        vrayAttr = nodeSocket.vray_attr

        socketParams[vrayAttr] = WriteConnectedNode(bus, nodetree, nodeSocket, returnDefault=returnDefault)

    pluginModule = PLUGINS[vrayType][vrayPlugin]

    # XXX: Used to access 'image' pointer for BitmapBuffer
    # and 'texture' for TexGradRamp and TexRemap
    #
    bus['context']['node'] = node

    result = ExportUtils.WritePlugin(
        bus,
        pluginModule,
        pluginName,
        propGroup,
        socketParams
    )

    return result


##     ##    ###    ######## ######## ########  ####    ###    ##
###   ###   ## ##      ##    ##       ##     ##  ##    ## ##   ##
#### ####  ##   ##     ##    ##       ##     ##  ##   ##   ##  ##
## ### ## ##     ##    ##    ######   ########   ##  ##     ## ##
##     ## #########    ##    ##       ##   ##    ##  ######### ##
##     ## ##     ##    ##    ##       ##    ##   ##  ##     ## ##
##     ## ##     ##    ##    ######## ##     ## #### ##     ## ########

def WriteVRayMaterialNodeTree(bus, ntree, force=False):
    scene = bus['scene']

    VRayScene = scene.vray
    SettingsOptions = VRayScene.SettingsOptions

    outputNode = GetNodeByType(ntree, 'VRayNodeOutputMaterial')
    if not outputNode:
        Debug("Output node not found!", msgType='ERROR')
        return bus['defaults']['material']

    # Check global material override
    #
    if 'material_override' in bus:
        if bus['material_override'] is not None and outputNode.dontOverride == False:
            return bus['material_override']
    
    # Check connection
    #
    materialSocket = outputNode.inputs['Material']
    if not materialSocket.is_linked:
        Debug("NodeTree: %s" % ntree.name, msgType='ERROR')
        Debug("  Node: %s" % outputNode.name, msgType='ERROR')
        Debug("  Error: Material socket is not connected!", msgType='ERROR')
        return bus['defaults']['material']

    return WriteConnectedNode(bus, ntree, materialSocket)
