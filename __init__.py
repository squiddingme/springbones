bl_info = {
    "name": "Spring Bones",
    "author": "Artell",
    "version": (0, 9, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Bones",
    "description": "Add a spring dynamic effect to a single/multiple bones",    
    "category": "Animation"}

if "bpy" in locals():
    from importlib import reload
    if "spring_bones" in locals():
        reload(spring_bones)
else:
    from .spring_bones import *

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()