from django.shortcuts import render
from django.views.decorators.http import require_POST
from main.utils import check_item_for_like, get_session_key
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User
from .serializers import ItemSerializer

from profiling.models import Item


def index(request):
    template = "home/index.html"
    return render(request, template)


@require_POST
def like(request):
    if request.user.is_authenticated:
        return check_item_for_like(request)

    else:
        session_key = get_session_key(request)
        return check_item_for_like(request, session_key)


def explore(request):
    template = "home/explore.html"
    items = Item.objects.select_related("owner").all()
    context = {
        "items": items
    }
    return render(request, template, context)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(methods=['get'], detail=True)
    def author(self, request, pk):
        author = User.objects.get(pk=pk)
        return Response({'author': author.username})
