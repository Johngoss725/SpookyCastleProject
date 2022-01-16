import bpy
import os 

# This script will RNR Render And Rotate
# This loop her loops through our animations.  

for action in bpy.data.actions:
    bpy.ops.object.mode_set(mode='OBJECT')
    
    #selected objects returns a list of objects we have currently selected in the 3D viewport. 
    #We should have our armature selected for this script to work. 
    bpy.context.selected_objects[0].animation_data.action = action
    
    
    currAction = bpy.context.selected_objects[0].animation_data.action
    use_num = currAction.frame_range
    
    use_string = action.name
    #Place the folder you want to render the files to here it will create seperate folders with the animations names.  
    
    use_path = "/home/testing_user/Documents/AnimationHolder/"
    os.mkdir(use_path+use_string)
    bpy.context.scene.frame_end = use_num.y

    if use_num.y<=25:
        print("less than 25 frames")
        bpy.context.scene.frame_step = 1
        
    if use_num.y>=25 and use_num.y<50:
        print("less than 50 frames")
        bpy.context.scene.frame_step = 2
        
    if use_num.y>=50 and use_num.y<100:
        print("less than 100 frames")
        bpy.context.scene.frame_step = 4
        
    if use_num.y>=100 and use_num.y<150:
        print("less than 150 frames")
        bpy.context.scene.frame_step = 5
        
    if use_num.y>=150:
        print("more than than 25 frames")
        bpy.context.scene.frame_step = 6
    
    print("**********************************************************")
    print("Action: ", action.name)
    print("Frames: ", use_num.y)
    print("Frame Step: ", bpy.context.scene.frame_step)
    print("**********************************************************")
    
    #This loop rotates our armature to the right degree and renders the animation. The degree is not incremented it is set to the specific dimension. 
    for i in range(8):
    
        if i == 0:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"Left"

        if i == 1:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"DownLeft"
    
        if i == 2:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"Down"
    
        if i == 3:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"DownRight"##
    
        if i == 4:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"Right"
    
        if i == 5:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"UpRight"
    
        if i == 6:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"Up"
    
        if i == 7:
            bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.scene.render.filepath = "/home/testing_user/Documents/AnimationHolder/"+use_string+"/"+use_string+"UpLeft"

        bpy.ops.render.render(animation=True, write_still=True)
        print("We are on loop: ", i ) 