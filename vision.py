from google.cloud import vision
import io


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
                for word in paragraph.words:
                    full = [''.join([symbol.text for symbol in word.symbols])]
                    words += full
                paragraph_data[count] = {"confidence": paragraph.confidence, "Bounding": paragraph.bounding_box, "Words": \
                    words}
        
                count += 1
                            
    print(paragraph_data[0])    

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
#detect_document("IMG_6361.jpg")