import os
#IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")
#NAVIGA NEL FILE SYSTEM
def CercaStringaInFilename(sFilename,sStringToSearch):
    sFilename = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    print("Cerco {1} in {0} ".format(sFilename,sStringToSearch1))
    iRet = sFilename.find(sStringToSearch1)
    if(iRet>-1):
        print("Trovato")
        return True
    return False

import PyPDF2


def CercaInFilePdf(sFile,sString):
    object = PyPDF2.PdfReader(sFile)
    numPages = len(object.pages)
    for i in range(0, numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        text = text.lower()
        if(text.find(sString)!=-1):
            return True
    return False


def CercaStringaInFileContent(sFilePathCompleto, sString):
    OutFileName,sOutFileExt = os.path.splitext(sFilePathCompleto)
    if(sOutFileExt.lower()==".pdf"):
        #print("Riconosciuto file pdf " + sFile)
        return CercaInFilePdf (sFilePathCompleto,sString)


iNumFileTrovati = 0

for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(sToPrint)
    for filename in files:
        iRet = CercaStringaInFilename(filename,sStringaDaCercare)
        if(iRet != True):
            sFilePathCompleto = os.path.join(root, filename)
            iRet = CercaStringaInFileContent(sFilePathCompleto, sStringaDaCercare)
        if(iRet == True):
            print("Trovato file: ",filename)
            iNumFileTrovati = iNumFileTrovati + 1
