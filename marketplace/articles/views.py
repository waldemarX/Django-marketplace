from django.shortcuts import render
from .models import Post


def articles(request):
    template = 'articles/articles.html'
    posts = Post.objects.filter(is_published=True).order_by('-pub_date')
    context = {
        'posts': posts,
        'subtitle': 'Articles',
        'dark': True
    }
    return render(request, template, context)


def article_detail(request, article_id):
    template = 'articles/article-detail.html'
    post_details = Post.objects.get(pk=article_id)
    context = {
        'post': post_details,
        'subtitle': post_details.title,
        'dark': True
    }
    return render(request, template, context)
