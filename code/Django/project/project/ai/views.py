from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
import os
import json
from .models import Image
from .func import text_detection, google_object
import base64

@api_view(['GET'])
def index(request):
    return render(request, 'index.html')
    # return Response("index")

@api_view(['POST'])
def textDetection(request):
    request = json.loads(request.body)
    header, encoded = request['image'].split(",", 1)

    list = text_detection.detection(encoded)
    result = dict()
    result['data'] = list
    with open('text_result.jpg', "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode('utf-8')
    result['image'] = my_string
    return Response(result)

@api_view(['POST'])
def objectDetection(request):
    request = json.loads(request.body)
    header, encoded = request['image'].split(",", 1)

    list = google_object.run(encoded)
    result = dict()
    result['data'] = list
    with open('object_result.jpg', "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode('utf-8')
    result['image'] = my_string

    # roi_list = []
    # for f in os.listdir('result/'):
    #     with open('result/' + f, "rb") as img_file:
    #         my_string = base64.b64encode(img_file.read()).decode('utf-8')
    #     roi_list.append(my_string)
    #
    # result['roi'] = roi_list
    return Response(result)