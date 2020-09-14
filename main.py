import shutil
import os

directory = "/Users/Gustaf/downloads"

#source = "pycharm-community-2020.2.1.dmg"
#destination = "test_folder"

#file_change = shutil.move(source, destination)
#print(file_change)

"""
for fileName in os.listdir(directory):
    if fileName.endswith(".dmg"):
        source = fileName
        destination = "dmg_folder"
        file_change = shutil.move(source, destination)
        print(file_change)
"""

file_type_list = []
for filename in os.listdir("/Users/Gustaf/downloads"): #insert your downloads folder path
    path = directory
    file_type = os.path.splitext(filename)[1]
    if file_type in file_type_list:
        continue
    if file_type not in file_type_list:
        file_type_list.append(file_type)
        #newPath = os.path.join(directory, file_type)
        try:
            print(directory + file_type.replace(".", "/"))
            os.mkdir(directory + file_type.replace(".", "/"))
        except OSError as error:
            print(error)

# när python hittar en fil, för en IF - IF (filtyp hittad): gör en mapp åt den filtypen.
# IF (filtypen har redan en mapp): lägg filen i rätt mapp
# kolla upp hur man får ett script att va konstant igång

