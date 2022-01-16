import os
from tilesheet_creator import Tilesheet_Maker
from parser import Godot_Parser

source_path = ("/home/testing_user/Documents/AnimationHolder/pirate_anims")
output_loc = ("/home/testing_user/Documents/GodotParser/godot_parser/TestingGodot/TestingSpritesheets/Pirate_stuff")
'''
This script will take in our source(our parent folder that holds our animation folders) and will produce
spritesheets in our output location(where are spritesheet will be stored).
Additionally the parser class will require an output location where our .tscn file will be built.
'''
#We use this to pass data to our Godot Parser
datadict = {}

# this holds our animation names
anim_name_dict = {}

# this will hold our total frames per animation in a list format. 
num_dict = {}

# holds our tilesheet objects. 
sheet_dict =  {}

my_array = []
# This loop returns our folders in the parent folder in the first index of an array 
# my_array=[[folder, folder, folder, ...,][][]]
for root,anim_folders,files in os.walk(source_path):
    my_array.append(anim_folders)

TOTAL_file_num = len(my_array[0])

# This loop iterates through the folders that house our PNG's and creates tilesheets from them.  
for n in range(len(my_array[0])):
    
    sheet_dict["sheet{0}".format(n)] = Tilesheet_Maker(source_path, output_loc, n)
    
    use_dict = sheet_dict["sheet{0}".format(n)].create_tilesheet()
    
    num_dict["num{0}".format(n)] = use_dict["num"]
    anim_name_dict["anim_name{0}".format(n)] = use_dict["anim_name"]

datadict["TOTAL_FILE_NUM"] = TOTAL_file_num
datadict["SOURCE"] = output_loc

'''
To deal with creating the animations dynamically inside the godot scene we need certain information that we 
pass in in the form of a dictionary. 

NUM wll be a list containg the amount of frames in each folder.
ANIM will be a list containg the folders name that houses the individual PNG's
SOURCE will be the location of our Spritesheets. 
TOTAL_FILE_NUM total numbers of fiole in the folder
'''
datadict['NUM'] = []
datadict['ANIM'] = []

for fileNum in range(TOTAL_file_num):
    
    datadict["NUM"].append(num_dict["num{fNum}".format(fNum = fileNum)])
    
    datadict["ANIM"].append(anim_name_dict["anim_name{fNum}".format(fNum = fileNum)])
    
GDParser = Godot_Parser(datadict)
print(GDParser)
