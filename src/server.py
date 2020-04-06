from flask import Flask, request, render_template
from evaluate import evaluate
from util import downloadImages, removeFiles, downloadImage, removeFile, getBase64
import os, io

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
app = Flask(__name__)


@app.route('/eval/images', methods=['POST'])
def images():
    try:
        urlList = request.get_json()["urlList"]
        localFilePathList = downloadImages(urlList)
        result = list(evaluate(localFilePathList, "image"))
        removeFiles(localFilePathList)
        return {'score': result}
    except Exception as e:
        removeFiles(localFilePathList)
        return {'error': str(e)}

@app.route('/eval/image', methods=['GET'])
def image():
    try:
        url = request.args.get('url')
        for key in request.args:
            if key != 'url':
                url += '&' + key + '=' + request.args[key]
        localFilePath = downloadImage(url)
        score = list(evaluate([localFilePath], "image"))
        imageData = getBase64(localFilePath)
        result = render_template("index.html", imageData=imageData, score=score[0])
        removeFile(localFilePath)
        return result
    except Exception as e:
        removeFile(localFilePath)
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)