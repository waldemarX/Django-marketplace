from django.shortcuts import render
from .models import Post


def articles(request):
    template = 'articles/articles.html'
    articles = Post.objects.filter(is_published=True).order_by('pub_date')
    context = {
        'articles': articles
    }
    return render(request, template, context)


def article_detail(request, article_id):
    template = 'articles/article-detail.html'
    context = {}
    return render(request, template, context)
