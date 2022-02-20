from flask import Flask, jsonify, send_file
import json


from data_struct import *
from gVision import *

app = Flask(__name__)

@app.route("/data")
def hello_world():
    data = detect_document("IMG_6361.jpg")
    #print(data)
    for key in data.keys():
        if key != "color":
            imgPut(data[key]["Bounding"], data["color"])
    for key in data.keys():
        if key != "color":
            print(data[key]["Words"])
            sentence = " ".join(data[key]["Words"])
            print(sentence)
            trans_sent = translate_text("es",sentence)
            imgSet(trans_sent, data[key]["Bounding"])
    return send_file("IMG_6361.jpg", mimetype='image')


