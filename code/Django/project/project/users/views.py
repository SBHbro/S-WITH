from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # 응답하는 메서드
from rest_framework.decorators import api_view  # 요청 방식을 필터링
from .models import User, Voca
from .serializers import UserSerializer, VocaSerializer
from django.core.serializers import serialize
import json

@api_view(['POST'])
def user_insert(request):
    if request.method == 'POST':
        users = User.objects.all()
        data = json.loads(serialize('json',users))
        req = json.loads(request.body)
        id = req['id']

        pk = User.objects.filter(id=id)

        if not pk.exists():
            print("null")
            serializer = UserSerializer(data=request.data)
            if(serializer.is_valid(raise_exception=True)):
                serializer.save()
            return Response(serializer.data)
        else:
            user = get_object_or_404(User, pk=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

@api_view(['GET'])
def user_vocaList(request, user_pk):
    if request.method == 'GET':
        vocaList = Voca.objects.filter(user_id=user_pk)
        serializer = VocaSerializer(vocaList, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def voca_list(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = VocaSerializer(data=request.data)  # JSON => python
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=data['user_id'])
        return Response(serializer.data)

@api_view(['DELETE'])
def voca_detail(request,voca_pk):
    if request.method == 'DELETE':
        voca = get_object_or_404(Voca, pk=voca_pk)
        voca.delete()
        return Response({'message': '성공적으로 삭제되었습니다.'})