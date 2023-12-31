from django.shortcuts import render


def news_page(request):
    template = 'news/news.html'
    return render(request, template)
