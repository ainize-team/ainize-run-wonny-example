
import os, base64
from urllib.request import urlopen
import string 
import random
import requests

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

class DownloadPrecheckFailed(Exception):
    pass

DOWNLOAD_MAX_SIZE = 5 * 1024 * 1024

def downloadImage(url):
    localFilePath =  IMAGE_PATH + '/' + getRandomStr(15) + '.jpg'
    r = requests.get(url, stream=True)
    # Precheck
    content_type = r.headers.get('Content-Type')
    if not content_type or content_type not in (
        'image/jpeg',
        'image/jpg',
        'image/png',
    ):
        raise DownloadPrecheckFailed('Non-image url is not supported.')
    content_length = int(r.headers.get('Content-Length', 0))
    if not content_length or content_length > DOWNLOAD_MAX_SIZE:
        raise DownloadPrecheckFailed('Size of file should be less than 5Mb.')
    downloaded_size = 0
    with open(localFilePath, 'wb') as handler:
        for data in r.iter_content():
            handler.write(data)
            downloaded_size += len(data)
            if downloaded_size > DOWNLOAD_MAX_SIZE:
                raise DownloadPrecheckFailed('Size of file should be less than 5Mb.')
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