import io
import os
import cv2
import numpy as np
from data_struct import * 
from PIL import ImageFont, ImageDraw, Image


def translate_text(target, text):

   # target = "es"
   # text = "Good Morning"
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    #print("test")
    #print(u"Text: {}".format(result["input"]))
   # print(u"Translation: {}".format(result["translatedText"]))
   # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return (result["translatedText"])

def imgPut(vertices, color, file):
    img = cv2.imread(file)
    xs = [i[0] for i in vertices]
    minX = min(xs)
    maxX = max(xs)
    ys = [i[1] for i in vertices]
    minY = min(ys)
    maxY = max(ys)
    img[minY:maxY,minX:maxX] = (color[2],color[1],color[0])
    blur = cv2.blur(img,(30,30))
    cv2.imwrite("IMG_6361.jpg",img)

def imgSet(txt, vertices,file):
    img = cv2.imread(file)
    xs = [i[0] for i in vertices]
    minX = min(xs)
    maxX = max(xs)
    ys = [i[1] for i in vertices]
    minY = min(ys)
    maxY = max(ys)
    fontpath = "SIMSUN.ttf"
    font = ImageFont.truetype(fontpath, 25)
    img_pil = Image.open(file)
    draw = ImageDraw.Draw(img_pil)
    draw.text((minX,((minY+maxY)/2)), txt, font = font, fill = (0,0,0,0))
    img_pil.save(file)

