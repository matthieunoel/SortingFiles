import os
import ntpath
# import time
# import datetime
from pathlib import Path
from tinytag import TinyTag
import shutil

# def getListOfFiles(dirname) :
#     listOfFile = os.listdir(dirname)
#     allFiles = list()

#     for entry in listOfFile :
#         fullPath = os.path.join(dirname, entry)
#         if os.path.isdir(fullPath):
#             allFiles = allFiles + getListOfFiles(fullPath)
#         else:
#             allFiles.append(fullPath)
#     return allFiles

# def moveFile(From, To, inc) :

#     res = str()

#     if inc > 1:
#         input("PAUSE BEFORE")
#         ToBis = os.path.splitext(To)[0] + "(" + str(inc) + ")" + os.path.splitext(To)[1]
#         print(ToBis)
#         input("PAUSE AFTER")

#     if ntpath.exists(ToBis):
#         res = moveFile(From, ToBis, inc+1)

#     else:    
#         os.rename(From, ToBis)
#         # FilesList.append(os.path.join(SuperPath, ntpath.basename(target)))
#         res = ToBis

#     return res

SuperPath = input("[*] Veuillez saisir le chemin du tri : ")
# print("[*] Veuillez saisir le chemin du tri : ./Test")
# SuperPath = "./Test"
print("Chargement ...")

for FilePath in os.listdir(SuperPath):
    if ntpath.isfile(ntpath.join(SuperPath, FilePath)):
        try:
            Artiste = TinyTag.get(ntpath.join(SuperPath, FilePath)).artist
            FolderName = str(Artiste)
        except:
            print("(" + ntpath.basename(FilePath) + ") Erreur de lecture de l'artiste")
        else:
            try:
                FolderPath = os.path.join(SuperPath, FolderName)
                Path(FolderPath).mkdir(parents=True, exist_ok=True)
                os.rename(ntpath.join(SuperPath, FilePath), os.path.join(SuperPath, FolderName, ntpath.basename(FilePath)))
            except:
                print("(" + ntpath.basename(FilePath) + ") Erreur de déplacement")

# print("Fin du tri.")
