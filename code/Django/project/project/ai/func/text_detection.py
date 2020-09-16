import io # 파일을 읽고 쓰기위한 모듈
import os # os의 기능을 사용하기 위한 모듈

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import base64

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

    img = vision.types.Image(content=content)

    response = client.text_detection(image=img)
    texts = response.text_annotations

    list = []

    # print(texts)
    for text in texts:
        # print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        # print('bounds: {}'.format(','.join(vertices)))
        list.append(text.description)
    list.remove(list[0])
    return list