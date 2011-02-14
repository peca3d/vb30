'''

 V-Ray/Blender 2.5

 http://vray.cgdo.ru

 Author: Andrey M. Izrantsev (aka bdancer)
 E-Mail: izrantsev@gmail.com

 This plugin is protected by the GNU General Public License v.2

 This program is free software: you can redioutibute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is dioutibuted in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

 All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Group

'''


''' Blender modules '''
import bpy
from bpy.props import *

''' vb modules '''
from vb25.utils import *
from vb25.ui.ui import *

class VRaySlot(bpy.types.IDPropertyGroup):
	pass

bpy.types.Texture.vray_slot= PointerProperty(
	name= "V-Ray Material Texture Slot",
	type=  VRaySlot,
	description= "V-Ray material texture slot settings."
)

VRaySlot.uvwgen= StringProperty(
	name= "UVW Generator",
	subtype= 'NONE',
	options= {'HIDDEN'},
	description= "UVW generator name.",
	default= "UVWGenChannel_default"
)

VRaySlot.blend_mode= EnumProperty(
	name= "Blend mode",
	description= "Blend mode.",
	items= (
		('NONE',        "None",       ""),
		('OVER',        "Over",       ""),
		('IN',          "In",         ""),
		('OUT',         "Out",        ""),
		('ADD',         "Add",        ""),
		('SUBTRACT',    "Subtract",   ""),
		('MULTIPLY',    "Multiply",   ""),
		('DIFFERENCE',  "Difference", ""),
		('LIGHTEN',     "Lighten",    ""),
		('DARKEN',      "Darken",     ""),
		('SATURATE',    "Saturate",   ""),
		('DESATUREATE', "Desaturate", ""),
		('ILLUMINATE',  "Illuminate", ""),
	),
	default= 'NONE'
)

# VRayLight.map_= BoolProperty(
# 	name= "",
# 	description= ".",
# 	default= False
# )
# VRaySlot._mult= FloatProperty(
# 	name= " texture multiplier",
# 	description= " texture multiplier.",
# 	min= 0.0,
# 	max= 100.0,
# 	soft_min= 0.0,
# 	soft_max= 1.0,
# 	default= 1.0
# )
# VRaySlot.map_diffuse= BoolProperty(
# 	name= "Diffuse",
# 	description= "Diffuse texture.",
# 	default= False
# )
# VRaySlot.diffuse_mult= FloatProperty(
# 	name= "Diffuse texture multiplier",
# 	description= "Diffuse texture multiplier.",
# 	min= 0.0,
# 	max= 100.0,
# 	soft_min= 0.0,
# 	soft_max= 1.0,
# 	default= 1.0
# )

VRaySlot.texture_rotation_h= FloatProperty(
	name= "Horiz. rotation",
	description= "Horizontal rotation.",
	min= -360.0,
	max= 360.0,
	soft_min= -180.0,
	soft_max= 180.0,
	default= 0.0
)

VRaySlot.texture_rotation_v= FloatProperty(
	name= "Vert. rotation",
	description= "TODO.",
	min= -360.0,
	max= 360.0,
	soft_min= -180.0,
	soft_max= 180.0,
	default= 0.0
)

VRaySlot.map_displacement= BoolProperty(
	name= "Displacement",
	description= "Displacement texture.",
	default= False
)

VRaySlot.displacement_mult= FloatProperty(
	name= "Displacement texture multiplier",
	description= "Displacement texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_normal= BoolProperty(
	name= "Normal",
	description= "Normal texture.",
	default= False
)

VRaySlot.normal_mult= FloatProperty(
	name= "Normal texture multiplier",
	description= "Normal texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_opacity= BoolProperty(
	name= "Opacity",
	description= "Opacity texture.",
	default= False
)

VRaySlot.opacity_mult= FloatProperty(
	name= "Opacity texture multiplier",
	description= "Opacity texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_roughness= BoolProperty(
	name= "Roughness",
	description= "Roughness texture.",
	default= False
)

VRaySlot.roughness_mult= FloatProperty(
	name= "Roughness texture multiplier",
	description= "Roughness texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_reflect= BoolProperty(
	name= "Reflection",
	description= "Reflection texture.",
	default= False
)

VRaySlot.reflect_mult= FloatProperty(
	name= "Reflection texture multiplier",
	description= "Reflection texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_reflect_glossiness= BoolProperty(
	name= "Reflection glossiness",
	description= "Reflection glossiness texture.",
	default= False
)

VRaySlot.reflect_glossiness_mult= FloatProperty(
	name= "Reflection glossiness texture multiplier",
	description= "Reflection glossiness texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_hilight_glossiness= BoolProperty(
	name= "Hilight glossiness",
	description= "Hilight glossiness texture.",
	default= False
)

VRaySlot.hilight_glossiness_mult= FloatProperty(
	name= "Hilight glossiness texture multiplier",
	description= "Hilight glossiness texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_anisotropy= BoolProperty(
	name= "Anisotropy",
	description= "Anisotropy texture.",
	default= False
)

VRaySlot.anisotropy_mult= FloatProperty(
	name= "Anisotropy texture multiplier",
	description= "Anisotropy texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_anisotropy_rotation= BoolProperty(
	name= "Anisotropy rotation",
	description= "Anisotropy rotation texture.",
	default= False
)

VRaySlot.anisotropy_rotation_mult= FloatProperty(
	name= "Anisotropy rotation texture multiplier",
	description= "Anisotropy rotation texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_fresnel_ior= BoolProperty(
	name= "Fresnel IOR",
	description= "Fresnel IOR texture.",
	default= False
)

VRaySlot.fresnel_ior_mult= FloatProperty(
	name= "Fresnel IOR texture multiplier",
	description= "Fresnel IOR texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_refract= BoolProperty(
	name= "Refraction",
	description= "Refraction texture.",
	default= False
)

VRaySlot.refract_mult= FloatProperty(
	name= "Refraction texture multiplier",
	description= "Refraction texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_refract_ior= BoolProperty(
	name= "Refraction IOR",
	description= "Refraction IOR texture.",
	default= False
)

VRaySlot.refract_ior_mult= FloatProperty(
	name= "Refraction IOR texture multiplier",
	description= "Refraction IOR texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_refract_glossiness= BoolProperty(
	name= "Refraction glossiness",
	description= "Refraction glossiness texture.",
	default= False
)

VRaySlot.refract_glossiness_mult= FloatProperty(
	name= "Refraction glossiness texture multiplier",
	description= "Refraction glossiness texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_translucency_color= BoolProperty(
	name= "Translucency",
	description= "Translucency texture.",
	default= False
)

VRaySlot.translucency_color_mult= FloatProperty(
	name= "Translucency texture multiplier",
	description= "Translucency texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)


'''
  BRDFSSS2Complex
'''
VRaySlot.map_overall_color= BoolProperty(
	name= "Overall color",
	description= "Overall color.",
	default= False
)

VRaySlot.overall_color_mult= FloatProperty(
	name= "Overall color multiplier",
	description= "Overall color multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_diffuse_color= BoolProperty(
	name= "Diffuse color",
	description= "Diffuse color.",
	default= False
)

VRaySlot.diffuse_color_mult= FloatProperty(
	name= "Diffuse color multiplier",
	description= "Diffuse color multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_diffuse_amount= BoolProperty(
	name= "Diffuse amount",
	description= "Diffuse amount.",
	default= False
)

VRaySlot.diffuse_amount_mult= FloatProperty(
	name= "Diffuse amount multiplier",
	description= "Diffuse amount multiplie.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_sub_surface_color= BoolProperty(
	name= "Sub-surface color",
	description= "Sub-surface color.",
	default= False
)

VRaySlot.sub_surface_color_mult= FloatProperty(
	name= "Sub-surface color multiplier",
	description= "Sub-surface color multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_scatter_radius= BoolProperty(
	name= "Scatter radius",
	description= "Scatter radius.",
	default= False
)

VRaySlot.scatter_radius_mult= FloatProperty(
	name= "Scatter radius multiplier",
	description= "Scatter radius multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_specular_color= BoolProperty(
	name= "Specular color",
	description= "Specular color.",
	default= False
)

VRaySlot.specular_color_mult= FloatProperty(
	name= "Specular color multiplier",
	description= "Specular color multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_specular_amount= BoolProperty(
	name= "Specular amount",
	description= "Specular amoun.",
	default= False
)

VRaySlot.specular_amount_mult= FloatProperty(
	name= "Specular amount multiplier.",
	description= "Specular amount multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)

VRaySlot.map_specular_glossiness= BoolProperty(
	name= "Specular glossiness",
	description= "Specular glossiness.",
	default= False
)

VRaySlot.specular_glossiness_mult= FloatProperty(
	name= "Specular glossiness multiplier.",
	description= "Specular glossiness multiplier.",
	min=0.0,
	max=100.0,
	soft_min=0.0,
	soft_max=1.0,
	default=1.0
)


'''
  EnvironmentFog
'''
VRaySlot.map_emission_tex= BoolProperty(
	name= "Emission",
	description= "Emission texture.",
	default= False
)

VRaySlot.emission_tex_mult= FloatProperty(
	name= "Emission texture multiplier",
	description= "Emission texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_color_tex= BoolProperty(
	name= "Color",
	description= "Color texture.",
	default= False
)

VRaySlot.color_tex_mult= FloatProperty(
	name= "Color texture multiplier",
	description= "Color texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_density_tex= BoolProperty(
	name= "Density",
	description= "Density texture.",
	default= False
)

VRaySlot.density_tex_mult= FloatProperty(
	name= "Density texture multiplier",
	description= "Density texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRaySlot.map_fade_out_tex= BoolProperty(
	name= "Fade out",
	description= "Fade out texture.",
	default= False
)

VRaySlot.fade_out_tex_mult= FloatProperty(
	name= "Fade out texture multiplier",
	description= "Fade out texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)


class VRayLight(bpy.types.IDPropertyGroup):
	pass

VRaySlot.VRayLight= PointerProperty(
	name= "VRayLight",
	type=  VRayLight,
	description= "VRay lights texture slot settings."
)

VRayLight.map_color= BoolProperty(
	name= "Color",
	description= "A color texture that if present will override the \"Color\" parameter.",
	default= True
)

VRayLight.color_mult= FloatProperty(
	name= "Color texture multiplier",
	description= "Color texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRayLight.map_shadowColor= BoolProperty(
	name= "Shadow",
	description= "A color texture that if present will override the \"Shadow color\" parameter.",
	default= False
)

VRayLight.shadowColor_mult= FloatProperty(
	name= "Shadow color texture multiplier",
	description= "Shadow color texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

VRayLight.map_intensity= BoolProperty(
	name= "Intensity",
	description= "A color texture that if present will override the \"Intensity\" parameter.",
	default= False
)

VRayLight.intensity_mult= FloatProperty(
	name= "Intensity texture multiplier",
	description= "Intensity texture multiplier.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

# Seems that we could use tex from "color"
# VRayLight.map_rect= BoolProperty(
# 	name= "Rectangle",
# 	description= "The light texture.",
# 	default= False
# )

# Seems that we could use tex from "color"
# VRayLight.map_dome= BoolProperty(
# 	name= "Dome",
# 	description= ".",
# 	default= False
# )


class GeomDisplacedMesh(bpy.types.IDPropertyGroup):
	pass

VRaySlot.GeomDisplacedMesh= PointerProperty(
	name= "GeomDisplacedMesh",
	type=  GeomDisplacedMesh,
	description= "GeomDisplacedMesh texture slot settings."
)

GeomDisplacedMesh.type= EnumProperty(
	name= "Type",
	description= "Displacement type.",
	items= (
		('2D',  "2D",     "2D displacement."),
		('NOR', "Normal", "Normal displacement."),
		('3D',  "Vector", "Vector displacement.")
	),
	default= 'NOR'
)

GeomDisplacedMesh.displacement_amount= FloatProperty(
	name= "Amount",
	description= "Displacement amount.",
	min= -100.0,
	max= 100.0,
	soft_min= -0.1,
	soft_max= 0.1,
	precision= 5,
	default= 0.02
)

GeomDisplacedMesh.displacement_shift= FloatProperty(
	name="Shift",
	description="",
	min=-100.0,
	max=100.0,
	soft_min=-1.0,
	soft_max=1.0,
	precision=4,
	default=0.0
)

GeomDisplacedMesh.water_level= FloatProperty(
	name="Water level",
	description="",
	min=-100.0, max=100.0, soft_min=-1.0, soft_max=1.0,
	default=0.0
)

GeomDisplacedMesh.use_globals= BoolProperty(
	name= "Use globals",
	description= "If true, the global displacement quality settings will be used.",
	default= True
)

GeomDisplacedMesh.view_dep= BoolProperty(
	name= "View dependent",
	description= "Determines if view-dependent tesselation is used",
	default= True
)

GeomDisplacedMesh.edge_length= FloatProperty(
	name= "Edge length",
	description= "Determines the approximate edge length for the sub-triangles",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 10.0,
	precision= 3,
	default= 4
)

GeomDisplacedMesh.max_subdivs= IntProperty(
	name= "Max subdivs",
	description= "Determines the maximum subdivisions for a triangle of the original mesh",
	min= 0,
	max= 2048,
	soft_min= 0,
	soft_max= 1024,
	default= 256
)

GeomDisplacedMesh.keep_continuity= BoolProperty(
	name= "Keep continuity",
	description= "If true, the plugin will attempt to keep the continuity of the displaced surface",
	default= False
)

GeomDisplacedMesh.map_channel= IntProperty(
	name= "Map channel",
	description= "The mapping channel to use for vector and 2d displacement.",
	min= 0,
	max= 100,
	soft_min= 0,
	soft_max= 10,
	default= 1
)

GeomDisplacedMesh.use_bounds= BoolProperty(
	name= "Use bounds",
	description= "If true, the min/max values for the displacement texture are specified by the min_bound and max_bound parameters; if false, these are calculated automatically.",
	default= False
)

GeomDisplacedMesh.min_bound= FloatVectorProperty(
	name= "Min bound",
	description= "The lowest value for the displacement texture",
	subtype= 'COLOR',
	min= 0.0,
	max= 1.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= (0,0,0)
)

GeomDisplacedMesh.max_bound= FloatVectorProperty(
	name= "Max bound",
	description= "The biggest value for the displacement texture",
	subtype= 'COLOR',
	min= 0.0,
	max= 1.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= (1,1,1)
)

GeomDisplacedMesh.resolution= IntProperty(
	name= "Resolution",
	description= "Resolution at which to sample the displacement map for 2d displacement.",
	min= 0,
	max= 2048,
	soft_min= 0,
	soft_max= 512,
	default= 256
)

GeomDisplacedMesh.precision= IntProperty(
	name= "Precision",
	description= "Increase for curved surfaces to avoid artifacts.",
	min= 0,
	max= 100,
	soft_min= 0,
	soft_max= 10,
	default= 8
)

GeomDisplacedMesh.tight_bounds= BoolProperty(
	name= "Tight bounds",
	description= "When this is on, initialization will be slower, but tighter bounds will be computed for the displaced triangles making rendering faster.",
	default= False
)

GeomDisplacedMesh.filter_texture= BoolProperty(
	name= "Filter texture",
	description= "Filter the texture for 2d displacement.",
	default= False
)

GeomDisplacedMesh.filter_blur= FloatProperty(
	name= "Blur",
	description= "The amount of UV space to average for filtering purposes. A value of 1.0 will average the whole texture.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 10.0,
	precision= 3,
	default= 0.001
)


class BRDFBump(bpy.types.IDPropertyGroup):
	pass

VRaySlot.BRDFBump= PointerProperty(
	name= "BRDFBump",
	type=  BRDFBump,
	description= "BRDFBump texture slot settings."
)

BRDFBump.bump_tex_mult= FloatProperty(
	name= "Amount",
	description= "Bump amount.",
	min= 0.0,
	max= 100.0,
	soft_min= 0.0,
	soft_max= 10.0,
	precision= 3,
	default= 0.02
)

BRDFBump.map_type= EnumProperty(
	name= "Map type",
	description= "Normal map type.",
	items= (
		('EXPLICIT', "Normal (explicit)", "."),
		('WORLD',    "Normal (world)",    "."),
		('CAMERA',   "Normal (camera)",   "."),
		('OBJECT',   "Normal (object)",   "."),
		('TANGENT',  "Normal (tangent)" , "."),
		('BUMP',     "Bump",              ".")
	),
	default= 'BUMP'
)

BRDFBump.bump_shadows= BoolProperty(
	name= "Bump shadows",
	description= "Offset the surface shading point, in addition to the normal.",
	default= False
)

BRDFBump.compute_bump_for_shadows= BoolProperty(
	name= "Transparent bump shadows",
	description= "True to compute bump mapping for shadow rays in case the material is transparent; false to skip the bump map for shadow rays (faster rendering).",
	default= True
)



'''
  GUI
'''

def context_tex_datablock(context):
    idblock= context.material
    if idblock:
        return idblock

    idblock= context.lamp
    if idblock:
        return idblock

    idblock= context.world
    if idblock:
        return idblock

    idblock= context.brush
    return idblock


def base_poll(cls, context):
	rd= context.scene.render
	tex= context.texture
	if tex is None:
		return False
	return ((tex.type != 'NONE' or tex.use_nodes) and (rd.engine in cls.COMPAT_ENGINES))


class VRayTexturePanel():
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'texture'

	@classmethod
	def poll(cls, context):
		tex= context.texture
		return tex and (tex.type != 'NONE' or tex.use_nodes) and (context.scene.render.engine in cls.COMPAT_ENGINES)


class VRAY_TEX_context(VRayTexturePanel, bpy.types.Panel):
	bl_label       = ""
	bl_options     = {'HIDE_HEADER'}
	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		engine = context.scene.render.engine
		if not hasattr(context, "texture_slot"):
			return False
		return ((context.material or context.world or context.lamp or context.brush or context.texture)
			and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		layout = self.layout
		slot = context.texture_slot
		node = context.texture_node
		space = context.space_data
		tex = context.texture
		idblock = context_tex_datablock(context)
		pin_id = space.pin_id

		if not isinstance(pin_id, bpy.types.Material):
			pin_id = None

		if not space.use_pin_id:
			layout.prop(space, "texture_context", expand=True)

		tex_collection = (not space.use_pin_id) and (node is None) and (not isinstance(idblock, bpy.types.Brush))

		if tex_collection:
			row = layout.row()

			row.template_list(idblock, "texture_slots", idblock, "active_texture_index", rows=2)

			col = row.column(align=True)
			col.operator("texture.slot_move", text="", icon='TRIA_UP').type = 'UP'
			col.operator("texture.slot_move", text="", icon='TRIA_DOWN').type = 'DOWN'
			col.menu("TEXTURE_MT_specials", icon='DOWNARROW_HLT', text="")

		split = layout.split(percentage=0.65)
		col = split.column()

		if tex_collection:
			col.template_ID(idblock, "active_texture", new="texture.new")
		elif node:
			col.template_ID(node, "texture", new="texture.new")
		elif idblock:
			col.template_ID(idblock, "texture", new="texture.new")

		if pin_id:
			col.template_ID(space, "pin_id")

		col = split.column()

		if tex:
			split = layout.split(percentage=0.2)

			if tex.use_nodes:

				if slot:
					split.label(text="Output:")
					split.prop(slot, "output_node", text="")

			else:
				split.label(text="Texture:")
				split.prop(tex, "type", text="")
				if tex.type == 'VRAY':
					split= layout.split()
					col= split.column()
					col.prop(tex.vray, 'type', text="Type")


import properties_texture
properties_texture.TEXTURE_PT_preview.COMPAT_ENGINES.add('VRAY_RENDER')
properties_texture.TEXTURE_PT_preview.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_texture.TEXTURE_PT_image.COMPAT_ENGINES.add('VRAY_RENDER')
properties_texture.TEXTURE_PT_image.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
del properties_texture


class VRAY_TEX_influence(VRayTexturePanel, bpy.types.Panel):
	bl_label = "Influence"
	
	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		engine= context.scene.render.engine
		tex= context.texture
		if not hasattr(context, "texture_slot"):
			return False
		return (tex and (context.material or context.world or context.lamp or context.brush or context.texture)
				and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		def factor_but(layout, slot, toggle, factor, label= None):
			row= layout.row(align=True)
			row.prop(slot, toggle, text="")
			sub= row.row()
			sub.active= getattr(slot,toggle)
			if label:
				sub.prop(slot, factor, slider=True, text=label)
			else:
				sub.prop(slot, factor, slider=True)

		layout= self.layout
		wide_ui= context.region.width > narrowui

		idblock= context_tex_datablock(context)

		slot= context.texture_slot
		texture= slot.texture

		VRaySlot= texture.vray_slot

		if type(idblock) == bpy.types.Material:
			ma= context.material
			VRayMaterial= ma.vray


			if VRayMaterial.type == 'BRDFVRayMtl':
				split= layout.split()
				col= split.column()
				col.label(text="Diffuse:")
				split= layout.split()
				col= split.column()
				factor_but(col, slot,     'use_map_color_diffuse', 'diffuse_color_factor', "Diffuse")
				factor_but(col, VRaySlot, 'map_roughness',         'roughness_mult',       "Roughness")
				if wide_ui:
					col= split.column()
				factor_but(col, slot,     'use_map_alpha',         'alpha_factor',         "Alpha")

				split= layout.split()
				col= split.column()
				col.label(text="Reflection:")
				split= layout.split()
				col= split.column()
				factor_but(col, slot,     'use_map_raymir',         'raymir_factor',           "Reflect")
				factor_but(col, VRaySlot, 'map_reflect_glossiness', 'reflect_glossiness_mult', "Glossiness")
				factor_but(col, VRaySlot, 'map_hilight_glossiness', 'hilight_glossiness_mult', "Hilight")
				if wide_ui:
					col= split.column()
				factor_but(col, VRaySlot, 'map_anisotropy',          'anisotropy_mult',          "Anisotropy")
				factor_but(col, VRaySlot, 'map_anisotropy_rotation', 'anisotropy_rotation_mult', "Rotation")
				factor_but(col, VRaySlot, 'map_fresnel_ior',         'fresnel_ior_mult',         "Fresnel IOR")

				split= layout.split()
				col= split.column()
				col.label(text="Refraction:")
				split= layout.split()
				col= split.column()
				factor_but(col, VRaySlot, 'map_refract',            'refract_mult',            "Refract")
				factor_but(col, VRaySlot, 'map_translucency_color', 'translucency_color_mult', "Translucency")
				if wide_ui:
					col= split.column()
				factor_but(col, VRaySlot, 'map_refract_ior',        'refract_ior_mult',        "IOR")
				factor_but(col, VRaySlot, 'map_refract_glossiness', 'refract_glossiness_mult', "Glossiness")

			elif VRayMaterial.type == 'BRDFSSS2Complex':
				split= layout.split()
				col= split.column()
				col.label(text="SSS:")
				split= layout.split()
				col= split.column()
				factor_but(col, slot,     'use_map_color_diffuse', 'diffuse_color_factor',   "Overall")
				factor_but(col, VRaySlot, 'map_sub_surface_color', 'sub_surface_color_mult', "Sub-surface")
				if wide_ui:
					col= split.column()
				factor_but(col, VRaySlot, 'map_scatter_radius',    'scatter_radius_mult',    "Scatter radius")

				layout.separator()

				split= layout.split()
				col= split.column()
				factor_but(col, VRaySlot, 'map_diffuse_color',  'diffuse_color_mult',  "Diffuse")
				factor_but(col, VRaySlot, 'map_diffuse_amount', 'diffuse_amount_mult', "Amount")
				if wide_ui:
					col= split.column()
				factor_but(col, VRaySlot, 'map_specular_color',      'specular_color_mult',      "Specular")
				factor_but(col, VRaySlot, 'map_specular_amount',     'specular_amount_mult',     "Amount")
				factor_but(col, VRaySlot, 'map_specular_glossiness', 'specular_glossiness_mult', "Glossiness")

			elif VRayMaterial.type == 'BRDFLight':
				split= layout.split()
				col= split.column()
				col.label(text="Diffuse:")
				split= layout.split()
				col= split.column()
				factor_but(col, slot, 'use_map_color_diffuse', 'diffuse_color_factor', "Diffuse")
				if wide_ui:
					col= split.column()
				factor_but(col, slot, 'use_map_alpha', 'alpha_factor', "Alpha")

			# elif VRayMaterial.type == 'VOL':
			# 	split= layout.split()
			# 	col= split.column()
			# 	col.label(text="Volume:")
			# 	split= layout.split()
			# 	col= split.column()
			# 	factor_but(col, VRaySlot, 'map_color_tex',    'color_tex_mult',    "Color")
			# 	factor_but(col, VRaySlot, 'map_density_tex',  'density_tex_mult',  "Density")
			# 	if wide_ui:
			# 		col= split.column()
			# 	factor_but(col, VRaySlot, 'map_emission_tex', 'emission_tex_mult', "Emission")

			if VRayMaterial.type in ('BRDFVRayMtl','BRDFSSS2Complex'):
				layout.separator()

				BRDFBump= VRaySlot.BRDFBump

				layout.label(text="Bump / Normal:")

				split= layout.split()
				col= split.column()
				row= col.row(align=True)
				row.prop(slot, 'use_map_normal', text="")
				sub= row.row()
				sub.active= getattr(slot,'use_map_normal')
				sub.prop(VRaySlot, 'normal_mult', slider=True, text="Normal")
				if wide_ui:
					col= split.column()
				col.active= slot.use_map_normal
				col.prop(BRDFBump,'map_type',text="Type")
				col.prop(BRDFBump,'bump_tex_mult')
				col.prop(BRDFBump,'bump_shadows')
				col.prop(BRDFBump,'compute_bump_for_shadows')

			GeomDisplacedMesh= VRaySlot.GeomDisplacedMesh

			layout.label(text="Geometry:")

			split= layout.split()
			col= split.column()
			factor_but(col, VRaySlot, 'map_displacement', 'displacement_mult', "Displace")
			if wide_ui:
				col= split.column()
			col.active= VRaySlot.map_displacement
			col.prop(GeomDisplacedMesh, 'type')
			col.prop(GeomDisplacedMesh, 'displacement_amount', slider=True)

		elif issubclass(type(idblock), bpy.types.Lamp):
			VRayLight= VRaySlot.VRayLight

			split= layout.split()
			col= split.column()
			factor_but(col, VRayLight, 'map_color', 'color_mult', "Color")
			factor_but(col, VRayLight, 'map_shadowColor', 'shadowColor_mult', "Shadow")
			if wide_ui:
				col= split.column()
			factor_but(col, VRayLight, 'map_intensity', 'intensity_mult', "Intensity")

		elif type(idblock) == bpy.types.World:
			split= layout.split()
			col= split.column()
			col.label(text="Environment:")
			factor_but(col, slot, 'use_map_blend',       'blend_factor',       "Background")
			if wide_ui:
				col= split.column()
			col.label(text="Override:")
			factor_but(col, slot, 'use_map_horizon',     'horizon_factor',     "GI")
			factor_but(col, slot, 'use_map_zenith_up',   'zenith_up_factor',   "Reflections")
			factor_but(col, slot, 'use_map_zenith_down', 'zenith_down_factor', "Refractions")

		layout.separator()

		split= layout.split()
		col= split.column()
		col.label(text="Options:")
		split= layout.split()
		col= split.column()
		col.prop(VRaySlot,'blend_mode',text="Blend")
		if wide_ui:
			col= split.column()
		col.prop(slot,'invert',text="Invert")
		col.prop(slot,'use_stencil')


class VRAY_TEX_displacement(VRayTexturePanel, bpy.types.Panel):
	bl_label = "Displacement"
	
	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		idblock= context_tex_datablock(context)
		if not type(idblock) == bpy.types.Material:
			return False

		texture_slot= getattr(context,'texture_slot',None)
		if not texture_slot:
			return False

		texture= texture_slot.texture
		if not texture:
			return False
		
		VRaySlot= texture.vray_slot
		return (base_poll(__class__, context) and VRaySlot.map_displacement)

	def draw(self, context):
		layout= self.layout
		wide_ui= context.region.width > narrowui

		texture_slot= getattr(context,'texture_slot',None)
		texture= texture_slot.texture if texture_slot else context.texture

		if texture:
			VRaySlot= texture.vray_slot

			if VRaySlot:
				GeomDisplacedMesh= VRaySlot.GeomDisplacedMesh

				split= layout.split()
				col= split.column()
				col.prop(GeomDisplacedMesh, 'displacement_shift', slider=True)
				col.prop(GeomDisplacedMesh, 'water_level', slider=True)
				col.prop(GeomDisplacedMesh, 'resolution')
				col.prop(GeomDisplacedMesh, 'precision')
				if wide_ui:
					col= split.column()
				col.prop(GeomDisplacedMesh, 'keep_continuity')
				col.prop(GeomDisplacedMesh, 'use_bounds')
				if GeomDisplacedMesh.use_bounds:
					sub= col.row()
					sub.prop(GeomDisplacedMesh, 'min_bound', text="Min")
					sub.prop(GeomDisplacedMesh, 'max_bound', text="Max")
				col.prop(GeomDisplacedMesh, 'filter_texture')
				if GeomDisplacedMesh.filter_texture:
					col.prop(GeomDisplacedMesh, 'filter_blur')

				split= layout.split()
				col= split.column()
				col.prop(GeomDisplacedMesh, 'use_globals')
				if not GeomDisplacedMesh.use_globals:
					split= layout.split()
					col= split.column()
					col.prop(GeomDisplacedMesh, 'edge_length')
					col.prop(GeomDisplacedMesh, 'max_subdivs')
					if wide_ui:
						col= split.column()
					col.prop(GeomDisplacedMesh, 'view_dep')
					col.prop(GeomDisplacedMesh, 'tight_bounds')


class VRAY_TEX_mapping(VRayTexturePanel, bpy.types.Panel):
	bl_label = "Mapping"

	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		tex= context.texture
		engine= context.scene.render.engine
		return (tex and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		layout= self.layout
		wide_ui= context.region.width > narrowui

		idblock= context_tex_datablock(context)

		sce= context.scene
		ob= context.object

		slot= getattr(context,'texture_slot',None)
		tex= slot.texture if slot else context.texture

		VRayTexture= tex.vray
		VRaySlot= tex.vray_slot

		if type(idblock) == bpy.types.Material:
			if wide_ui:
				layout.prop(VRayTexture, 'texture_coords', expand=True)
			else:
				layout.prop(VRayTexture, 'texture_coords')

			if VRayTexture.texture_coords == 'UV':
				if slot:
					split= layout.split(percentage=0.3)
					split.label(text="Layer:")
					if ob and ob.type == 'MESH':
						split.prop_search(slot, 'uv_layer', ob.data, 'uv_textures', text="")
					else:
						split.prop(slot, 'uv_layer', text="")
			else:
				split= layout.split(percentage=0.3)
				split.label(text="Projection:")
				split.prop(VRayTexture, 'mapping', text="")
				split= layout.split(percentage=0.3)
				split.label(text="Object:")
				split.prop_search(VRayTexture, 'object', sce, 'objects', text="")

		elif type(idblock) == bpy.types.World:
			split= layout.split(percentage=0.3)
			split.label(text="Projection:")
			split.prop(VRayTexture, 'environment_mapping', text="")

			split= layout.split()
			col= split.column()
			col.prop(VRaySlot, 'texture_rotation_h')
			if wide_ui:
				col= split.column()
			col.active= False
			col.prop(VRaySlot, 'texture_rotation_v')

		if slot:
			split= layout.split()
			col= split.column()
			col.prop(slot, 'offset')
			if wide_ui:
				col= split.column()
			sub= col.column()
			sub.active= 0
			sub.prop(slot, 'scale')


class VRAY_TEX_image(VRayTexturePanel, bpy.types.Panel):
	bl_label = "Texture"

	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		tex= context.texture
		engine= context.scene.render.engine
		return tex and ((tex.type == 'IMAGE' and tex.image) and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		layout= self.layout
		wide_ui= context.region.width > narrowui

		slot= getattr(context,'texture_slot',None)
		tex= slot.texture if slot else context.texture

		VRayTexture= tex.vray

		if wide_ui:
			layout.prop(VRayTexture, 'tile', expand=True)
		else:
			layout.prop(VRayTexture, 'tile')

		if VRayTexture.tile != 'NOTILE':
			split = layout.split()
			col= split.column()
			col.label(text="Tile:")
			sub= col.row(align=True)
			sub_u= sub.row()
			sub_u.active= VRayTexture.tile in ('TILEUV','TILEU')
			sub_u.prop(tex, 'repeat_x', text='U')
			sub_v= sub.row()
			sub_v.active= VRayTexture.tile in ('TILEUV','TILEV')
			sub_v.prop(tex, 'repeat_y', text='V')
			if wide_ui:
				col= split.column()
			col.label(text="Mirror:")
			sub= col.row(align=True)
			sub_u= sub.row()
			sub_u.active= VRayTexture.tile in ('TILEUV','TILEU')
			sub_u.prop(tex, 'use_mirror_x', text='U')
			sub_v= sub.row()
			sub_v.active= VRayTexture.tile in ('TILEUV','TILEV')
			sub_v.prop(tex, 'use_mirror_y', text='V')

		layout.separator()

		if wide_ui:
			layout.prop(VRayTexture, 'placement_type', expand=True)
		else:
			layout.prop(VRayTexture, 'placement_type')

		split = layout.split()
		col= split.column()
		col.label(text="Crop Minimum:")
		sub= col.row(align=True)
		sub.prop(tex, 'crop_min_x', text='U')
		sub.prop(tex, 'crop_min_y', text='V')
		if wide_ui:
			col= split.column()
		col.label(text="Crop Maximum:")
		sub= col.row(align=True)
		sub.prop(tex, 'crop_max_x', text='U')
		sub.prop(tex, 'crop_max_y', text='V')


class VRAY_TEX_bitmap(VRayTexturePanel, bpy.types.Panel):
	bl_label = "Bitmap"

	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		tex= context.texture
		engine= context.scene.render.engine
		return tex and ((tex.type == 'IMAGE' and tex.image) and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		layout= self.layout
		wide_ui= context.region.width > narrowui

		slot= getattr(context,'texture_slot',None)
		tex= slot.texture if slot else context.texture

		BitmapBuffer= tex.image.vray.BitmapBuffer

		split= layout.split()
		col= split.column()
		col.prop(BitmapBuffer, 'color_space')

		split= layout.split()
		col= split.column()
		col.prop(BitmapBuffer, 'filter_type', text="Filter")
		if BitmapBuffer.filter_type != 'NONE':
			col.prop(BitmapBuffer, 'filter_blur')
		if BitmapBuffer.filter_type == 'MIPMAP':
			col.prop(BitmapBuffer, 'interpolation', text="Interp.")
		if wide_ui:
			col= split.column()
		col.prop(BitmapBuffer, 'use_input_gamma')
		if not BitmapBuffer.use_input_gamma:
			col.prop(BitmapBuffer, 'gamma')
			#col.prop(BitmapBuffer, 'gamma_correct')
		col.prop(BitmapBuffer, 'allow_negative_colors')
		col.prop(BitmapBuffer, 'use_data_window')