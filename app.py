from flask import Flask, jsonify
import json


from data_struct import *
from gVision import *

app = Flask(__name__)

@app.route("/data")
def hello_world():
    data = detect_document("IMG_6361.jpg")
    print(data)
    for key in data.keys():
        sentence = " ".join(data[key]["Words"])
        print(sentence)
        trans_sent = translate_text("es",sentence)
        imgPut(trans_sent, data[key]["Bounding"])


