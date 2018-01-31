from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    article = models.Article.objects.get(pk=1);
    title = article.title
    content = article.content
    articles = models.Article.objects.all();
    #return render(request, 'blog/index.html', {'hello': 'hello dict!','title':title,'content':content,'article':article});
    return render(request,'blog/index.html',{'articles':articles});

#内容详情页
def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article});

#添加稿件
def add_page(request):
    return render(request,'blog/add_page.html');

#添加稿件操作
def add_page_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    models.Article.objects.create(title=title,content=content)

    articles = models.Article.objects.all();
    return render(request,'blog/index.html',{'articles':articles})

#编辑稿件
def edit_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_page_action(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = models.Article.objects.get(pk=id)
    article.title = title
    article.content = content
    article.save()
    article = models.Article.objects.get(pk=id)
    return render(request,'blog/article_page.html',{'article':article})
