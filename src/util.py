
import os, base64
from urllib.request import urlopen
import string 
import random 

def getRandomStr(length):
    string_pool = string.ascii_lowercase
    result = "" 
    for _ in range(length):
        result += random.choice(string_pool) 
    return result

IMAGE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/images"

def removeFile(filePath):
    try:
        if os.path.exists(filePath):
            os.remove(filePath)
    except:
        pass

def removeFiles(filePaths):
    try:
        for filePath in filePathList:
            removeFile(filePath)
    except:
        pass

def downloadImage(url):
    with urlopen(url) as res:
        res_data = res.read()
        localFilePath =  IMAGE_PATH + '/' + getRandomStr(15) + '.jpg'
        with open(localFilePath, 'wb') as f:
            f.write(res_data)
        return localFilePath

def downloadImages(urlList):
    localFilePaths = []
    for url in urlList:
        localFilePaths.append(downloadImage(url))
    return localFilePaths


def getBase64(localPath):
    with open(localPath, "rb") as imgFile:
        value = base64.b64encode(imgFile.read())
        return value.decode('utf-8')