from __future__ import print_function
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def img2Text(path):
    client = vision.ImageAnnotatorClient()    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)   
    text = response.full_text_annotation.text #여기 텍스트 변수 안에 변경된 텍스트가 들어갑니다.
    return text
