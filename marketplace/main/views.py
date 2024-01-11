import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from profiling.models import Item
from .models import Events


def index(request):
    template = 'home/index.html'
    return render(request, template)


@require_POST
def like(request):
    if request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            item = Item.objects.get(id=item_id)

            # If event from user is exists - like counter -= 1
            try:
                event = Events.objects.filter(user=request.user, object=item)
                if event.exists():
                    event = event.last()
                    if event.event == "Like":
                        event = Events(event="Dislike", user=request.user, object=item)
                        event.save()
                        item.likes -= 1
                        item.save(update_fields=['likes'])

                        return JsonResponse({'status': 'success', 'likes': item.likes, 'event': 'dislike'})

                    else:
                        event = Events(event="Like", user=request.user, object=item)
                        event.save()
                        item.likes += 1
                        item.save(update_fields=['likes'])
                else:
                    raise Events.DoesNotExist

            # If event from user is not exists - like counter += 1
            except Events.DoesNotExist:
                event = Events(event="Like", user=request.user, object=item)
                event.save()
                item.likes += 1
                item.save(update_fields=['likes'])

            return JsonResponse({'status': 'success', 'likes': item.likes, 'event': 'like'})

        except Item.DoesNotExist:

            return JsonResponse({'status': 'error', 'message': 'Post not found'})
