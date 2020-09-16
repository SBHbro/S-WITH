import io # 파일을 읽고 쓰기위한 모듈
import os # os의 기능을 사용하기 위한 모듈

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import base64
import cv2

def detection(image):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.dirname(os.path.abspath(__file__)) + '\\datasets\\My Project-070d5c77d071.json'
    client = vision.ImageAnnotatorClient()

    imgdata = base64.b64decode(image)
    path = 'text_detection.jpg'  # I assume you have a way of picking unique filenames
    with open(path, 'wb') as f:
        f.write(imgdata)

    # 이미지 읽기
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    new_img = cv2.imread(image)
    img = vision.types.Image(content=content)

    response = client.text_detection(image=img)
    texts = response.text_annotations

    list = []

    # print(texts)
    for idx,text in enumerate(texts):
        # print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        x = text.bounding_poly.vertices[0].x
        y = text.bounding_poly.vertices[0].y
        x2 = text.bounding_poly.vertices[2].x
        y2 = text.bounding_poly.vertices[2].y
        if idx != 0:
            cv2.rectangle(new_img, (x,y), (x2,y2), (255,0,0), 1)
        # cv2.rectangle(img, (10,10), (40,40), (255,0,0), 2)
        # print(vertices)
        list.append(text.description)
    list.remove(list[0])
    # cv2.imshow('result',img)
    # cv2.waitKey()
    return list