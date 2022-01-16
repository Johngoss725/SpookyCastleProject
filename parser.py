
import os

'''
This class will create a Godot .tscn file that can be used in the editor. It will rig an
animated sprite with the spritesheet we created previously. 
'''
class Godot_Parser():
    def __init__(self, datadict):
        self.source_path = datadict["SOURCE"]
        self.frames = datadict["NUM"]
        self.anim_name = datadict["ANIM"]
        self.total_sheets = datadict["TOTAL_FILE_NUM"]

        #This here allows us to retrieve the cont of animation frames
        #We may want to seperate this into a different function.  
        self.total = 0
        counter = 0
        for entries in self.frames:
            self.total += entries
            counter += 1
        self.total += (counter + 1)
        self.create_scene()
        
        
    def create_texture_element(self,f):
        counter = 0
        for i in range(len(self.anim_name)):
            f.write('[ext_resource path="res://TestingSpritesheets/Pirate_stuff/' +self.anim_name[counter] +'.png"'+ ' type="Texture" id=' + str(i + 1) + ']')
            f.write('\n')
            counter += 1

    def create_gd_header(self,f):
        f.write('[gd_scene load_steps=' + str((self.total + 2)) + ' format=2]')
        f.write('\n')
        f.write('\n')


    def create_scene(self):


        #***Location of our spritesheets***
        os.chdir(self.source_path)
        
        f = open('tester.tscn', 'w')
        self.create_gd_header(f)
        self.create_texture_element(f)
        f.write('\n')
        f.write('\n')
        
        
        master_counter = 0
        sub_id_counter = 1 
        for SpriteSheets in range(int(self.total_sheets)):
            countx = 0
            county = 0
            engaged = False

            #This loop here is creating this structure:
            '''
            [sub_resource type="AtlasTexture" id=1]
            flags = 4
            atlas = ExtResource( 1 )
            region = Rect2(0, 0, 128, 128)
            ''' 
            # this identifies to Godot a sub resource from our spritesheet. 

            for i in range(self.frames[master_counter]):
                # we may have to alter tis it works with two animations but we need a better way to update the sub counter. 
                if master_counter != 0 and not engaged:
                    engaged = True
                    sub_id_counter-=1
            
                use_x = countx * 128
                use_y = county * 128
                countx += 1
                
                if countx >= 16:
                    county += 1
                    countx = 0
                # print(i)
                f.write('[sub_resource type="AtlasTexture" id=' +str((sub_id_counter)) + "]" )
                f.write('\n')
                f.write('flags = 4')
                f.write('\n')
                f.write('atlas = ExtResource( ' + str(master_counter+1) + ' )')
                f.write('\n')
                f.write('region = Rect2(' + str(use_x) + ', ' + str(use_y) + ', 128, 128)')
                f.write('\n')
                f.write('\n')
                sub_id_counter += 1
            current_spriteframesId = str(sub_id_counter+1)
            
            sub_id_counter += 1

            f.write("\n")
            master_counter+=1
     
        f.write('[sub_resource type="SpriteFrames" id=' + current_spriteframesId + ']')
        f.write('\n')
        f.write('animations = [ {')
        f.write('\n')
        self.create_animation_element(f)
        
        
        f.write('[node name="ParsingTestingScene" type="Node2D"]')
        f.write("\n")
        f.write('\n')
        f.write('[node name="MySprite" type="AnimatedSprite" parent="."]')
        f.write("\n")
        f.write('frames = SubResource('+ current_spriteframesId +')')
        f.write('\n')
        f.write('animation = "TakeHitDownRight"')

        f.close()

        
        return("Complete")



    def create_animation_element(self,f):
        highest_num = 0
        dir_string = ""
        local_counter = 0
        p_counter = 0

        # for the length of the array we have in ANIM
        for x in range(len(self.anim_name)):
            frames = int(self.frames[x]/8)
            print("animation:", self.anim_name[x])
            print("frames:", frames)
            print("highest_num:", highest_num)
            storage_num = 1

            #alteration
            #if x!=0:
                #highest_num-= 1
            
            for i in range(8):
                # this array houses the raw text for concatentation into the file.         
                use_array = []
                if i == 0:
                    dir_string = "RightDown"
                if i == 1:
                    dir_string = "DownLeft"
                if i == 2:
                    dir_string = "Down"
                if i == 3:
                    dir_string = "Left"
                if i == 4:
                    dir_string = "UpRight"
                if i == 5:
                    dir_string = "LeftUp"
                if i == 6:
                    dir_string = "Up"
                if i == 7:
                    dir_string = "Right"

                if x == 0:
                    for n in range(frames):
                        use_string = " SubResource( " + str(storage_num) + " ) "
                        use_array.append(use_string)
                        storage_num += 1
                    highest_num = storage_num

                else:
                    for g in range(frames):
                        highest_num += 1
                        use_string =" SubResource( " + str(highest_num) + " ) "
                        use_array.append(use_string)
                #highest_num = storage_num

                sub_resource_string = ""
                use_counter = 0 
                
                for strings in use_array:
                    use_counter += 1
                    #here is what we changed 
                    if use_counter == frames:
                        sub_resource_string += strings 
                    else:
                        sub_resource_string += strings + ","
                if i!=0:
                    f.write('\n')
                else:
                    pass
                f.write('"frames":['+ sub_resource_string + '],')
                f.write('\n')
                f.write('"loop": true,')
                f.write('\n')
                #print(local_counter)
                #print(self.anim_name)
                f.write('"name": "'+ dir_string + self.anim_name[x] +'",')
                f.write('\n')
                f.write('"speed": 20.0')
                f.write('\n')
                f.write("")
                #print("here is our local counter at the spot",p_counter)
               # print("here is our second number" ,len(self.anim_name)*8)
                if (p_counter+1) != len(self.anim_name)*8:
                    f.write('},{ ')
                else:
                    f.write('} ]')
                p_counter+=1
            
            f.write('\n')
            f.write('\n')
            local_counter += 1


