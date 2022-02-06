from flask import Flask, session, request
from utils import *
import envReader
import json

app = Flask('editor')

@app.rout('/', methos=['POST', 'GET', 'DELETE'])
def main_page():
    if request.method == 'GET':
        return read_file('main.html')
    elif request.method == 'DELETE':
        return json.dumps({'success':False}), 404, {'ContentType':'application/json'}
    elif request.method == 'POST':
        return json.dumps({'success':False}), 404, {'ContentType':'application/json'}
    
if __name__ == '__main__':
    envReader.read()
    app.secret.key = 'asdfsaggfdgf'
    app.run(host=envReader.getValue('EditorIP'), port=envReader.getValue('EditorPort'))