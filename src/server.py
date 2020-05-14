from flask import Flask, request, render_template
from evaluate import evaluate
from util import downloadImage, removeFile, downloadImages, removeFiles
import os, io
from flask_cors import CORS
from flask import jsonify

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
app = Flask(__name__)
cors = CORS(app, resources={
  r"/eval/*": {"origin": "*"},
})

@app.route('/', methods=['GET'])
def main():
    return app.send_static_file('index.html')

@app.route('/healthz', methods=['GET'])
def healthz():
   return 'ok'

@app.route('/eval/images', methods=['POST'])
def images():
    localFilePathList = []
    try:
        urlList = request.get_json()["urlList"]
        if (len(urlList) > 10):
            return {'error': 'No more than 10.'}
        localFilePathList = downloadImages(urlList)
        result = list(evaluate(localFilePathList))
        removeFiles(localFilePathList)
        return {'score': result}
    except Exception as e:
        removeFiles(localFilePathList)
        return {'error': str(e)}

@app.route('/eval/image', methods=['get'])
def image():
    localFilePath = ''
    try:
        url = request.json["url"]
        localFilePath = downloadImage(url)
        score = list(evaluate([localFilePath]))
        return jsonify({'score': str(score[0])}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    finally:
        removeFile(localFilePath)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)