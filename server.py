from flask import Flask, request, jsonify, make_response, send_from_directory, render_template
from random import random
from flask_cors import CORS
import os
import shutil
from datetime import datetime
import pytz
from werkzeug.utils import secure_filename

import struct
from os import path
import warnings
import io


from pipeline_demo import demo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
CORS(app)

UPLOAD_DIR = 'upload'
PUBLIC_DIR = 'public'
API_ADDRESS = 'http://118.70.52.237:4801/'

def uploadFile(UPLOAD_DIR_,file):
    if not os.path.exists(UPLOAD_DIR_):
        os.makedirs(UPLOAD_DIR_)
    
    timeTerm: str = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) \
        .strftime('%Y%m%d%H%M%S')
    fileName: str = f'{timeTerm}-{file.filename}'
    fileName = secure_filename(fileName)
    filePath: str = os.path.join(UPLOAD_DIR_, fileName)
    file.save(filePath)
    return filePath

@app.route('/api/upload', methods=['POST'])
def upload():
    if len(request.files) == 0:
        return 'File upload is required.'
    #print('aaaaaaaaaaaaa',len(request.files))
    file1 = request.files['file1']
    try:
        shutil.rmtree(UPLOAD_DIR+'/data_sample')
        #shutil.rmtree(UPLOAD_DIR+'/data_vehicle')
    except:
        pass
    filePath1 = uploadFile(UPLOAD_DIR+'/data_sample',file1)
    file2 = request.files['file2']

    try:
        #shutil.rmtree(UPLOAD_DIR+'/data_sample')
        shutil.rmtree(UPLOAD_DIR+'/data_vehicle')
    except:
        pass
    filePath2 = uploadFile(UPLOAD_DIR+'/data_vehicle',file2)
    
    docInfo = demo(filePath1,filePath2,int(request.form['time_max_waiting']))
    return docInfo

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    docInfo = upload()
    return render_template('index.html', docInfo=docInfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=4802,
            threaded=True,
            debug=True)

