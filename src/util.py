
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
    try: 
        r = requests.get(url, stream=True)
    except Exception as e:
        raise DownloadPrecheckFailed(str(e))
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
        try:
            for url in urlList:
                localFilePaths.append(downloadImage(url))
        except Exception as e:
            localFilePaths.append(str(e))
            print(e, flush=True)
    return localFilePaths


def getBase64(localPath):
    with open(localPath, "rb") as imgFile:
        value = base64.b64encode(imgFile.read())
        return value.decode('utf-8')


def track_event(category, action, label=None, value=0):
    data = {
        'v': '1',  # API Version.
        'tid': 'UA-164242824-6',  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': '555',
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        'ua': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
    }

    response = requests.post(
        'https://www.google-analytics.com/collect', data=data)

    # If the request fails, this will raise a RequestException. Depending
    # on your application's needs, this may be a non-error and can be caught
    # by the caller.
    response.raise_for_status()