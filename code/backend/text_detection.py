# from PIL import Image
# from pytesseract import *
# import re
# import cv2
#
# img = Image.open('.\\datasets\\kakao.png')
# text = pytesseract.image_to_string(img,lang='kor')
# print(text)

import io # 파일을 읽고 쓰기위한 모듈
import os # os의 기능을 사용하기 위한 모듈

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=".\\datasets\\My Project-070d5c77d071.json"
client = vision.ImageAnnotatorClient()

# 이미지 읽기
with io.open('.\\datasets\\kakao.png', 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

# print(texts)
for text in texts:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print('bounds: {}'.format(','.join(vertices)))