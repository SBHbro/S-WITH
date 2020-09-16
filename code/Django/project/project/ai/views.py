from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
import os
from .models import Image

from .func import text_detection, google_object

@api_view(['POST'])
def textDetection(request):
    image = Image()
    image.images = request.FILES['images']
    image.save()
    address = os.path.dirname(os.path.abspath(__file__)) + '\\func\\datasets\\kakao.png'

    list = text_detection.detection(address)
    return Response(list)

@api_view(['POST'])
def objectDetection(request):
    image = Image()
    image.images = request.POST['imagebase64']
    image.save()
    address = os.path.dirname(os.path.abspath(__file__)) + '\\func\\datasets\\kakao.png'

    list = google_object.run()
    return Response(list)
