from flask import Flask, jsonify
import json

from vision import *

app = Flask(__name__)

@app.route("/data")
def data():
    response = app.response_class(
        response=json.dumps(detect_document("IMG_6361.jpg")),
        status=200,
        mimetype='application/json'
    )
    return response

