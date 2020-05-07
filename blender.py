# Blender-Architecture
import bpy

bpy.context.scene.cursor.location = (0,0,0)  
bpy.ops.mesh.archimesh_room() # Create ROOM
bpy.context.object.RoomGenerator[0].walls[0].w = 15 
bpy.context.object.RoomGenerator[0].wall_num = 4  
bpy.context.object.RoomGenerator[0].walls[1].w = 25 
bpy.context.object.RoomGenerator[0].walls[2].r = 180
bpy.context.object.RoomGenerator[0].walls[2].w = 15
bpy.context.object.RoomGenerator[0].walls[3].r = -90 
bpy.context.object.RoomGenerator[0].walls[3].w = 25

bpy.context.scene.cursor.location = (15,18,0)
bpy.ops.mesh.archimesh_room()
bpy.context.object.RoomGenerator[0].walls[0].r = -180
bpy.context.object.RoomGenerator[0].walls[0].w = 7
bpy.context.object.RoomGenerator[0].wall_num = 2 
bpy.context.object.RoomGenerator[0].walls[1].w = 7

bpy.context.scene.cursor.location = (0,19,0)
bpy.ops.mesh.archimesh_room()
bpy.context.object.RoomGenerator[0].walls[0].w = 5
bpy.context.object.RoomGenerator[0].wall_num = 2 
bpy.context.object.RoomGenerator[0].walls[1].w = 6

bpy.context.scene.cursor.location = (0,13,0)
bpy.ops.mesh.archimesh_room()
bpy.context.object.RoomGenerator[0].walls[0].w = 5
bpy.context.object.RoomGenerator[0].wall_num = 2 
bpy.context.object.RoomGenerator[0].walls[1].w = 6

bpy.context.scene.cursor.location = (15,13,0)
bpy.ops.mesh.archimesh_room()
bpy.context.object.RoomGenerator[0].walls[0].r = -180
bpy.context.object.RoomGenerator[0].walls[0].w = 3.5
bpy.context.object.RoomGenerator[0].wall_num = 2 
bpy.context.object.RoomGenerator[0].walls[1].w = 5

bpy.context.scene.cursor.location = (11.5,13,0)
bpy.ops.mesh.archimesh_room()
bpy.context.object.RoomGenerator[0].walls[0].r = -180
bpy.context.object.RoomGenerator[0].walls[0].w = 3.5
bpy.context.object.RoomGenerator[0].wall_num = 4 
bpy.context.object.RoomGenerator[0].walls[1].w = 3
bpy.context.object.RoomGenerator[0].walls[2].w = 2
bpy.context.object.RoomGenerator[0].walls[3].w = 2
