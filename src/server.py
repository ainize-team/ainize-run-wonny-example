from flask import Flask, request
import os
from urllib.request import urlopen
from evaluate import *
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
app = Flask(__name__)
IMAGE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/images"

def removeFiles(filePathList):
    try:
        for filePath in filePathList:
          os.remove(filePath)
    except:
        pass

@app.route('/eval', methods=['GET', 'POST'])
def eval():
    try:
        if (request.args.get('filePath')):
            filePathList = [request.args.get('filePath')]
        elif (request.get_json()["filePathList"]):
            filePathList = request.get_json()["filePathList"]
            
        print(filePathList)
        localFilePathList = []
        result = []
        for idx in range(len(filePathList)):
            with urlopen(filePathList[idx]) as res:
                res_data = res.read()
                localFilePath = IMAGE_PATH + "/" + str(idx) + ".jpg"
                with open(localFilePath, 'wb') as f:
                    f.write(res_data)
                localFilePathList.append(localFilePath)
        result = list(evaluate(localFilePathList, "image"))
        removeFiles(localFilePathList)
        return {'score': result}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)