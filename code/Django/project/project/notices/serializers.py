from rest_framework import serializers
from .models import Notice, Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id','user_id','notice_id','content','date']

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id','user_id','subject','content','email','date','url']
