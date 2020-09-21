from rest_framework import serializers
from .models import Notice

# serializer의 serilize는 '직렬화'
# serializer는 queryset, model instance와 같은 데이터를 JSON, XML 또는 다른 유형으로 변환할 수 있도록 해주는 역할

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id','subject','content','email','date']
