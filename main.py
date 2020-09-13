import shutil
import os

directory = "/Users/Gustaf/downloads"

#source = "pycharm-community-2020.2.1.dmg"
#destination = "test_folder"

#file_change = shutil.move(source, destination)
#print(file_change)


for fileName in os.listdir(directory):
    if fileName.endswith(".pdf"):
        source = fileName
        destination = "pdf_folder"
        file_change = shutil.move(source, destination)
        print(file_change)


# koppla python till downloads
# ge python åtkomst till downloads
# kör en while genom downloads, konstant
# när python hittar en fil, för en IF - IF (filtyp hittad): gör en mapp åt den filtypen.
# IF (filtypen har redan en mapp): lägg filen i rätt mapp
# kolla upp hur man får ett script att va konstant igång

