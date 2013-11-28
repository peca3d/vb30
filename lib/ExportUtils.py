#
# V-Ray For Blender
#
# http://vray.cgdo.ru
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

import os

import bpy

from vb25.debug import Debug, PrintDict

from . import utils, paths
from . import AttributeUtils


def WritePluginParams(bus, pluginModule, pluginName, propGroup, mappedParams):
    scene = bus['scene']
    o     = bus['output']

    if not hasattr(pluginModule, 'PluginParams'):
        Debug("Module %s doesn't have PluginParams!" % pluginModule.ID, msgType='ERROR')
        return

    for attrDesc in sorted(pluginModule.PluginParams, key=lambda t: t['attr']):
        attrName = attrDesc['attr']
        skip     = attrDesc.get('skip', False)

        if skip:
            continue

        # Skip output attributes
        if attrDesc['type'] in AttributeUtils.OutputTypes:
            continue

        # Type could be skipped, but mappedParams could contain a manually defined value for it
        if attrDesc['type'] in AttributeUtils.SkippedTypes and attrDesc['attr'] not in mappedParams:
            continue

        # Skip attibutes that should be mapped, but are not mapped,
        # we will use parameter value then
        if attrDesc['type'] in AttributeUtils.InputTypes and attrDesc['attr'] not in mappedParams:
            continue

        value = None

        if attrName in mappedParams:
            value = mappedParams[attrName]

        if value is None:
            value = getattr(propGroup, attrName)

        if value is None:
            Debug("%s.%s value is None!" % (pluginName, attrName), msgType='ERROR')
            continue

        if attrDesc['type'] in AttributeUtils.PluginTypes and not value:
            continue

        if attrDesc['type'] in {'STRING'}:
            if not value:
                continue
            else:
                subtype = attrDesc.get('subtype')
                if subtype in {'FILE_PATH', 'DIR_PATH'}:
                    # TODO: Copy file to the DR directory
                    value = paths.unifyPath(value)
                value = '"%s"' % value

        o.writeAttibute(attrName, value)


# Use this function from inside the module's 'writeDatablock'
def WritePluginCustom(bus, pluginModule, pluginName, propGroup, overrideParams):
    o = bus['output']

    o.set(pluginModule.TYPE, pluginModule.ID, pluginName)
    o.writeHeader()
    
    WritePluginParams(bus, pluginModule, pluginName, propGroup, overrideParams)

    o.writeFooter()

    return pluginName


def WritePlugin(bus, pluginModule, pluginName, propGroup, overrideParams):
    if hasattr(pluginModule, 'writeDatablock'):
        return pluginModule.writeDatablock(bus, pluginModule, pluginName, propGroup, overrideParams)

    WritePluginCustom(bus, pluginModule, pluginName, propGroup, overrideParams)

    return pluginName
