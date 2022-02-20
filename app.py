from flask import Flask, jsonify
import json


from vision import *

app = Flask(__name__)

@app.route("/data")
def hello_world():
    data = detect_document("IMG_6361.jpg")
    return data

