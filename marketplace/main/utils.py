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
            return add_event_like_or_dislike(item, session_key=session_key)
        else:
            return add_event_like_or_dislike(item, user=request.user)

    except Item.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Item not found",
            })


def add_event_like_or_dislike(item, session_key=None, user=None):
    try:
        event = Events.objects.filter(session_key=session_key, object=item, user=user)
        if event.exists():
            event = event.last()
            if event.event == "like":
                event = Events(event="dislike", user=user, session_key=session_key, object=item)
                item.likes -= 1
            else:
                event = Events(event="like", user=user, session_key=session_key, object=item)
                item.likes += 1
        else:
            raise Events.DoesNotExist
    except Events.DoesNotExist:
        event = Events(event="like", user=user, session_key=session_key, object=item)
        item.likes += 1

    event.save()
    item.save(update_fields=['likes'])
    return JsonResponse(
            {
                "status": "success",
                "likes": item.likes,
                "event": event.event,
            }
    )


def check_last_event(item, user=None, session_key=None):
    event = Events.objects.filter(session_key=session_key, object=item, user=user)
    if event.exists():
        event = event.last()
        if event.event == "like":
            return True
        else:
            return False
    else:
        return False


def check_if_like(request, item):
    if request.user.is_authenticated:
        return check_last_event(item, user=request.user)
    else:
        session_key = get_session_key(request)
        return check_last_event(item, session_key=session_key)
