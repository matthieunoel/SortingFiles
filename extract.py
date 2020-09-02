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

def MoveFile(From, To, Inc):
    
    res = str()
    OriTo = To
    
    if Inc > 0:
        To = ntpath.splitext(To)[0] + " (" + str(Inc) + ")" + ntpath.splitext(To)[1]

    if ntpath.exists(To):
        res = MoveFile(From, OriTo, Inc+1)
    else:
        os.rename(From, To)
        res = To

SuperPath = input("[*] Veuillez saisir le chemin du tri : ")
print("Chargement ...")

FilesList = getListOfFiles(SuperPath)

FilesListTemp = list()

# Mettre tout les fichiers dans ./

for FilePath in FilesList:
    if FilePath != os.path.join(SuperPath, ntpath.basename(FilePath)):
        res = MoveFile(FilePath, os.path.join(SuperPath, ntpath.basename(FilePath)), 0)
        FilesListTemp.append(res)

# Suppression de tout les dossiers de ./

for File in os.listdir(SuperPath):
    if os.path.isdir(os.path.join(SuperPath, File)):
        shutil.rmtree(os.path.join(SuperPath, File))

FilesList = FilesListTemp
