from google.cloud import vision
import io
import json
from google.protobuf.json_format import MessageToDict


def detect_document(path):
    """Detects document features in an image."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    

    paragraph_data = {}
    count = 0
    words = []

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))
            

            for paragraph in block.paragraphs:
                #print(paragraph)
                words = []
                count += 1
                print(count)
                for word in paragraph.words:
                    full = [''.join([symbol.text for symbol in word.symbols])]
                    print(full)
                    words += full
                box = []

                for i in list(paragraph.bounding_box.vertices):
                    X,Y = i.x, i.y
                    cords = (X,Y)
                    box.append(cords)
                
                paragraph_data[count] = {"confidence": paragraph.confidence, "Bounding": box, "Words": \
                    words}
        
                            
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return paragraph_data