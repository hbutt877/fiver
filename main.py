from flask import Flask, jsonify, render_template, request
import dropbox
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_from, file_to)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/postvideo',methods=['POST'])
def postvideo():
    transferData = TransferData('OF6GR3NX3fQAAAAAAAAAAS8S3eIa51ubPKoTKeeDFCvbnEiAUawjecXHPi0aVwfA')
    file_from = request.data
    file_to = '/test_dropbox/video'+str(int(time.time()))+'.mp4'
    transferData.upload_file(file_from, file_to)
    return jsonify('success')
