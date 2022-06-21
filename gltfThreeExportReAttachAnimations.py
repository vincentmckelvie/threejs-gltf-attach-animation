import bpy

def getAnimationByName(name):
    for a in bpy.data.actions:
        nm = a.name
        if nm == name:
            return a

for obj in bpy.data.objects:
    ani = getAnimationByName("Action_"+obj.name.lower()+"_"+obj.name.lower() )
    obj.animation_data_create()
    obj.animation_data.action = ani