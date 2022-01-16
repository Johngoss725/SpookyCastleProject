from PIL import Image
import os 

        

# we will pass this in source_path = ("/home/testing_user/Documents/Anims")
class Tilesheet_Maker():

    def __init__(self, anim_folder, output_loc,current_folder):
        self.anim_folder = anim_folder
        self.output_loc = output_loc
        self.folder_array = []
        self.debug_array = [[],[],[],[],[],[],[],[]]
        self.holder = [[],[],[],[],[],[],[],[]]
        self.current_folder = current_folder
        self.total_count = 0 
        

    def create_tilesheet(self):

        os.chdir(self.anim_folder)
        new_image = Image.new('RGBA',(2048,2048))
        # This will get an array of our folders in the source folder. 
        for root, dirs, files in os.walk(self.anim_folder,topdown="True"):
            for name in dirs:
                self.folder_array.append(name)

        # This will group each animation in an array by direction.
        for root, dir, files in os.walk(self.folder_array[self.current_folder]):
            for names in files:
                if "DownRight" in names:
                    self.debug_array[0].append(names)
                
                if "DownLeft" in names:
                    self.debug_array[1].append(names)
                
                if "Down" in names and not "DownLeft" in names and not "DownRight" in names:
                    self.debug_array[2].append(names)

                if "Left" in names and not "DownLeft" in names and not "UpLeft"in names:
                    self.debug_array[3].append(names)
                
                if "UpRight" in names:
                    self.debug_array[4].append(names)
                
                if "UpLeft" in names:
                    self.debug_array[5].append(names)
                
                if "Up" in names and not "UpLeft" in names and not "UpRight" in names:
                    self.debug_array[6].append(names)
                
                if "Right" in names and not "DownRight" in names and not "UpRight"in names:
                    self.debug_array[7].append(names)

        #This just sorts the 8 animation arrays so they will be in order. 
        for i in range(8):
            self.holder[i] = sorted(self.debug_array[i])
       # print(self.holder)
        #print(self.holder[0])
        counterx = 0
        countery = 0
        
        for arrays in self.holder:
            
            #print("******************")
            for pngs in arrays:
                self.total_count+=1
                #print(pngs)
                if counterx >= 16:
                    counterx = 0
                    countery += 1

                use_image = Image.open(self.anim_folder +"/"+ self.folder_array[self.current_folder] + "/" + pngs)
                new_image.paste(use_image,(counterx * 128, countery * 128))
                counterx += 1
        
        os.chdir(self.output_loc)
       # print(os.getcwd())
        new_image.save(self.folder_array[self.current_folder]+".png")
        
        use_dict={
                "num":self.total_count, 
                "anim_name":str(self.folder_array[self.current_folder])
                }
        return(use_dict)



                






