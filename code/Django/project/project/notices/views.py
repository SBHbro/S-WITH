from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
from .models import Notice
from .serializers import NoticeSerializer
import datetime

@api_view(['GET', 'POST'])
def notice_list(request):
    if request.method == 'GET':
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
    else:
        # 포스팅을 해달라고 하는 요청이 들어올 때는 data=request.data 사용
        serializer = NoticeSerializer(data=request.data)  # JSON => python
        if serializer.is_valid(raise_exception=True):
            # raise_exception: 검증에 실패시 400 bad request 응답을 주기 위함
            serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def notice_detail(request, notice_pk):
    if request.method == 'GET':
        notice = get_object_or_404(Notice, pk=notice_pk)
        serializer = NoticeSerializer(notice) # 객체 하나만 받기 때문에 many 필요없음
        return Response(serializer.data)
    elif request.method == 'PUT':
        notice = get_object_or_404(Notice, pk=notice_pk)
        notice.date = datetime.datetime.now()
        serializer = NoticeSerializer(data=request.data, instance=notice)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    else:
        notice = get_object_or_404(Notice, pk=notice_pk)
        notice.delete()
        return Response({'message': '성공적으로 삭제되었습니다.'})


