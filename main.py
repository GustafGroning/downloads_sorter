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
    path = "/Users/Gustaf/downloads"
    file_type = os.path.splitext(filename)[1]
    if file_type not in file_type_list:
        file_type_list.append(file_type)
print(file_type_list)



# koppla python till downloads
# ge python åtkomst till downloads
# kör en while genom downloads, konstant
# när python hittar en fil, för en IF - IF (filtyp hittad): gör en mapp åt den filtypen.
# IF (filtypen har redan en mapp): lägg filen i rätt mapp
# kolla upp hur man får ett script att va konstant igång

