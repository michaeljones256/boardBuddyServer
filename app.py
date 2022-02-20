from flask import Flask, jsonify, send_file, request, make_response
import json


from data_struct import *
from gVision import *

app = Flask(__name__)

@app.route("/data", methods=['POST', 'GET'])
def hello_world():
    file = request.files['file']
    file.save(file.filename)
    filename = file.filename
    data = detect_document(filename)

    #print(data)
    for key in data.keys():
        if key != "color":
            imgPut(data[key]["Bounding"], data["color"], filename)
    for key in data.keys():
        if key != "color":
            print(data[key]["Words"])
            sentence = " ".join(data[key]["Words"])
            print(sentence)
            trans_sent = translate_text("es",sentence)
            imgSet(trans_sent, data[key]["Bounding"], filename)
    return "hello"
    

@app.route("/data/response", methods=['GET'])
def filename_route():
    return send_file("IMG_6361.jpg", mimetype='image/jpg')
