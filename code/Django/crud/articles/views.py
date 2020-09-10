from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

# Article의 목록을 template에서 보여준다.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# /articles/create/
def create(request):
    # 입력을 받아서 article을 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST)        # 사용자의 입력을 폼에 담는다. 사용자가 입력한 데이터를 저장하는 폼
        if form.is_valid():                     # 유효한지 확인한다.
            article = form.save()               # 유효하다면 저장하고
            return redirect('articles:index')   # 유효하다면 redirect 한다.
    else:   # if request.method == 'GET':
        form = ArticleForm()                    # 빈 폼을 생성한다.

    context = {                                 # template에 보내주기 위해 context에 담는다.
        'form': form,                           # 반복되는 코드이기에 조건문을 조정하여 한 개의 코드로 만들어준다.
    }
    return render(request, 'articles/create.html', context) # templat응 render한다.


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)


# 주소로 받은 pk 값의 article을 삭제 후 index 페이지로 redirect
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')