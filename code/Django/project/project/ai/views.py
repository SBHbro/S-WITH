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


@api_view(['POST'])
def textDetection(request):
    request = json.loads(request.body)
    header, encoded = request['image'].split(",", 1)

    list = text_detection.detection(encoded)
    return Response(list)

@api_view(['POST'])
def objectDetection(request):
    request = json.loads(request.body)
    header, encoded = request['image'].split(",", 1)

    list = google_object.run(encoded)
    return Response(list)
