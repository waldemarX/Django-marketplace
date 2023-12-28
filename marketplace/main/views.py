from django.shortcuts import render


def index(request):
    template = 'main_page/index.html'
    return render(request, template)
