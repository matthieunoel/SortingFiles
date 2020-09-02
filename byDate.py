import os
import ntpath
import time
import datetime
from pathlib import Path

def getListOfFiles(dirname) :
    listOfFile = os.listdir(dirname)
    allFiles = list()

    for entry in listOfFile :
        fullPath = os.path.join(dirname, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

SuperPath = input("[*] Veuillez saisir le chemin du tri : ")
print("Chargement ...")
# SuperPath = "./TestFolder/"
# if SuperPath[-1] == "/" or SuperPath[-1] == "\\":
#     SuperPath
#     pass
# FilesList = list()
# SuperPath = SuperPath.rstrip('/')
# SuperPath = SuperPath.rstrip('\\')
# for target in getListOfFiles(SuperPath):
#     if ntpath.basename(target) != "desktop.ini":
#         os.rename(target, SuperPath + "/" + ntpath.basename(target))
#         FilesList.append(SuperPath + "/" + ntpath.basename(target))
#     else:
#         os.remove(target)

# for File in os.listdir(SuperPath):
#     if os.path.isdir(os.path.join(SuperPath, File)):
#         os.removedirs(os.path.join(SuperPath, File))

for File in os.listdir(SuperPath):
    FilePath = os.path.join(SuperPath, File)
    if ntpath.isdir(FilePath) != True:
        Date = os.path.getmtime(FilePath)
        FolderName = str(datetime.datetime.fromtimestamp(Date).year) + "-" + str(datetime.datetime.fromtimestamp(Date).month).zfill(2)
        FolderPath = os.path.join(SuperPath, FolderName)
        Path(FolderPath).mkdir(parents=True, exist_ok=True)
        os.rename(FilePath, os.path.join(SuperPath, FolderName, File))