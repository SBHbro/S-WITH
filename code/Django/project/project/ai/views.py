from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
import os


from .func import text_detection, google_object

@api_view(['GET'])
def textDetection(request):
    address = os.path.dirname(os.path.abspath(__file__)) + '\\func\\datasets\\kakao.png'

    list = text_detection.detection(address)
    return Response(list)

@api_view(['GET'])
def objectDetection(request):
    list = google_object.run()
    return Response(list)