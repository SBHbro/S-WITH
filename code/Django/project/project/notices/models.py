from django.db import models

# Create your models here.
class Notice(models.Model):
    # 모델의 기본키 필드는 별도로 지정하지 않으면 자동으로 추가된다.
    subject = models.CharField(max_length=100)
    content = models.TextField()
    email = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)