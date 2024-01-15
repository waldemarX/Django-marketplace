from django.shortcuts import render
from django.views.decorators.http import require_POST
from main.utils import check_item_for_like, get_session_key
from rest_framework import generics
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


class ItemApi(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
