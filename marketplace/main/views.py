import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from profiling.models import Item


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
            item.likes += 1
            item.save(update_fields=['likes'])
            return JsonResponse({'status': 'success', 'likes': item.likes})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Post not found'})
