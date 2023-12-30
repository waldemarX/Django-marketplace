from django.shortcuts import render


def profile(request):
    template = 'profiling/author.html'
    return render(request, template)


def collection(request):
    template = 'profiling/collection.html'
    return render(request, template)


def item(request):
    template = 'profiling/item-details.html'
    return render(request, template)
