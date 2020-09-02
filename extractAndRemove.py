import os
import ntpath
import shutil

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

# Mettre tout les fichiers dans ./

for FilePath in getListOfFiles(SuperPath):
    if ntpath.exists(os.path.join(SuperPath, ntpath.basename(FilePath))):
        os.remove(FilePath)
    else:
        os.rename(FilePath, os.path.join(SuperPath, ntpath.basename(FilePath)))

# Suppression de tout les dossiers de ./

for File in os.listdir(SuperPath):
    if os.path.isdir(os.path.join(SuperPath, File)):
        shutil.rmtree(os.path.join(SuperPath, File))
