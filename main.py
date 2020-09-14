import shutil
import os

directory = "/Users/Gustaf/downloads"

#source = "pycharm-community-2020.2.1.dmg"
#destination = "test_folder"

#file_change = shutil.move(source, destination)
#print(file_change)
"""
file_type_list = []
for filename in os.listdir("/Users/Gustaf/downloads"): #insert your downloads folder path
    path = directory
    file_type = os.path.splitext(filename)[1]
    if file_type in file_type_list:
        continue
    if file_type not in file_type_list:
        file_type_list.append(file_type)
        try:
            print(directory + file_type.replace(".", "/"))
            os.mkdir(directory + file_type.replace(".", "/"))
        except OSError as error:
            print(error)
"""

for filename in os.listdir("/Users/Gustaf/downloads"): 
    file_type = os.path.splitext(filename)[1]
    if file_type == ".txt":
        file_no_extension = os.path.splitext(filename)[0] #used for the full file path in shutil.move
        movable_file = "/Users/Gustaf/Downloads/" + "%s" % (filename)
        destination = "/Users/Gustaf/downloads/txt"
        shutil.move(movable_file, destination) 
    
    

#file = "/Users/Gustaf/Downloads/message.txt"
#destination = "/Users/Gustaf/downloads/txt"
#shutil.move(file, destination)

# TODO: kolla upp hur man får ett script att va konstant igång