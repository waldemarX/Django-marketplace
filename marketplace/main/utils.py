from django.http import JsonResponse
import json
from main.models import Events
from profiling.models import Item


def create_session_key(request):
    request.session.create()
    return request.session.session_key


def get_session_key(request):
    if not request.session.session_key:
        create_session_key(request)
        return request.session.session_key
    else:
        return request.session.session_key


def check_item_for_like(request, session_key=None):
    try:
        data = json.loads(request.body)
        item_id = data.get("item_id")
        item = Item.objects.get(id=item_id)

        if session_key:
            return add_event_like_or_dislike(request, item, session_key)
        else:
            return add_event_like_or_dislike(request, item)

    except Item.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Item not found",
            })


# def add_event_for_like(request, item, session_key=None,):
#     try:
#         event = Events.objects.filter(session_key=session_key, object=item, user=request.user)
#         if event.exists():
#             event = event.last()
#             if event.event == "like":
#                 event = Events(event="dislike", user=request.user, session_key=session_key, object=item)
#             else:
#                 event = Events(event="like", user=request.user, session_key=session_key, object=item)
#         else:
#             raise Events.DoesNotExist
#     except Events.DoesNotExist:
#         event = Events(event="like", user=request.user, session_key=session_key, object=item)


def add_event_like_or_dislike(request, item, session_key=None):
    try:
        if session_key:
            event = Events.objects.filter(session_key=session_key, object=item)
            if event.exists():
                event = event.last()
                if event.event == "like":
                    event = Events(event="dislike", session_key=session_key, object=item)
                else:
                    event = Events(event="like", session_key=session_key, object=item)
            else:
                raise Events.DoesNotExist
        else:
            event = Events.objects.filter(user=request.user, object=item)
            if event.exists():
                event = event.last()
                if event.event == "like":
                    event = Events(event="dislike", user=request.user, object=item)
                else:
                    event = Events(event="like", user=request.user, object=item)
            else:
                raise Events.DoesNotExist
    except Events.DoesNotExist:
        if session_key:
            event = Events(event="like", session_key=session_key, object=item)
        else:
            event = Events(event="like", user=request.user, object=item)

    event.save()
    if event.event == "like":
        item.likes += 1
    if event.event == "dislike":
        item.likes -= 1
    item.save(update_fields=['likes'])
    return JsonResponse(
            {
                "status": "success",
                "likes": item.likes,
                "event": event.event,
            }
    )


def check_if_like(request, item):
    if request.user.is_authenticated:
        event = Events.objects.filter(user=request.user, object=item)
        if event.exists():
            event = event.last()
            if event.event == "like":
                return True
            else:
                return False
        else:
            return False
    else:
        session_key = get_session_key(request)
        event = Events.objects.filter(session_key=session_key, object=item)
        if event.exists():
            event = event.last()
            if event.event == "like":
                return True
            else:
                return False
        else:
            return False
