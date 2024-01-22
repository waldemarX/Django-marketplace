from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import EventsSerializer, ItemSerializer
from main.utils import check_item_for_like, get_session_key
from main.models import Events
from users.models import User
from profiling.models import Item


class IndexView(TemplateView):
    template_name = "home/index.html"
    items = Item.objects.select_related("owner").all()
    users = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items_hot"] = self.items.order_by("-creation_date")[:6]
        context["items_pop"] = self.items.order_by("-likes")[:16]
        context["users"] = self.users.order_by("-balance")[:12]
        return context


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
    context = {"items": items}
    return render(request, template, context)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(methods=["get"], detail=True)
    def author(self, request, pk):
        author = User.objects.get(pk=pk)
        return Response({"author": author.username})


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    @action(methods=["get"], detail=False)
    def is_watched(self, request):
        events = Events.objects.filter(
            Q(user_receiver=request.user)
            & (Q(event="like") | Q(event="dislike"))
        )
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def clear(self, request):
        events = Events.objects.filter(
            Q(user_receiver=request.user)
            & (Q(event="like") | Q(event="dislike"))
            & Q(watch_status="False")
        )
        for event in events:
            event.watch_status = True
            event.save()
        return Response({"cleared": "200"})
