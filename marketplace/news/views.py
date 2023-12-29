from django.shortcuts import render


def news_page(request):
    template = 'news_page/news.html'
    return render(request, template)
