# b) Write a python program to create a ZIP file of a particular folder which containsseveral files inside it.

import os
import sys
import pathlib
import zipfile
dirName = input("Enter Directory name that you want to backup : ")
if not os.path.isdir(dirName):
        print("Directory", dirName, "doesn't exists")
        sys.exit(0)
curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w") as archive:
        for file_path in curDirectory.rglob("*"):
                archive.write(file_path, arcname=file_path.relative_to(curDirectory))
if os.path.isfile("myZip.zip"):
        print("Archive", "myZip.zip", "created successfully")
else:
        print("Error in creating zip archive")

# OUTPUT:
# Enter Directory name that you want to backup : New folder
# Archive myZip.zip created successfully