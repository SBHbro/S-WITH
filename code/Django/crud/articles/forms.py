from django import forms
from .models import Article

# 내부적으로 검증하는 프로그램?
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']