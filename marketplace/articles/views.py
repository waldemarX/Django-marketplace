from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Categories


def articles(request):
    template = 'articles/articles.html'
    page = request.GET.get('page', 1)
    posts = Post.objects.select_related('category').filter(is_published=True).order_by('-pub_date')
    categories = Categories.objects.all().order_by('category_name')
    paginator = Paginator(posts, per_page=6)
    current_page = paginator.page(page)
    context = {
        'posts': current_page,
        'categories': categories,
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
