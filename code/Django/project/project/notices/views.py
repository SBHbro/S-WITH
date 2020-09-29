from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
from .models import Notice, Reply
from .serializers import NoticeSerializer, ReplySerializer
import datetime
import json
import base64
from .forms import UploadFileForm

@api_view(['GET','POST'])
def notice_list(request):
    if request.method == 'GET':
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
    else:
        req = json.loads(request.body)
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=req['user_id'])
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def notice_detail(request, notice_pk):
    if request.method == 'GET':
        notice = get_object_or_404(Notice, pk=notice_pk)
        serializer = NoticeSerializer(notice)
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

@api_view(['GET'])
def notice_reply(request, notice_pk):
    if request.method == 'GET':
        replies = Reply.objects.filter(notice_id=notice_pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def reply_insert(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=req['user_id'], notice_id=req['notice_id'])
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def reply_detail(request, reply_pk):
    if request.method == 'GET':
        reply = get_object_or_404(Reply, pk=reply_pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    elif request.method == 'PUT':
        reply = get_object_or_404(Reply, pk=reply_pk)
        reply.date = datetime.datetime.now()
        serializer = ReplySerializer(data=request.data, instance=reply)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    elif request.method == 'DELETE':
        reply = get_object_or_404(Reply, pk=reply_pk)
        reply.delete()
        return Response({'message': '성공적으로 삭제되었습니다.'})

@api_view(['POST'])
def upload(request):
    request = json.loads(request.body)
    print(request)

    videodata = base64.b64decode(request['data'])
    fileName = request['filename'] + '.mp4'
    # print(videodata)
    path = 'upload/'+fileName  # I assume you have a way of picking unique filenames
    with open(path, 'wb') as f:
        f.write(videodata)
    f.close()
    return Response('success')