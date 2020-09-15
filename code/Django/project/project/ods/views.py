from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
import os

from .func import text_detection

@api_view(['GET'])
def imageUpload(request):
    print("=============================================")
    address = os.path.dirname(os.path.abspath(__file__)) + '\\func\\datasets\\kakao.png'

    text_detection.detection(address)
    return Response({'message': '성공적으로 삭제되었습니다.'})

