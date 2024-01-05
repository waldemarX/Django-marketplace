from django.db.models import Q
from .models import Post


def q_search(query):
    keywords = [word for word in query.split() if len(word) > 1]

    Q_objects = Q()

    for token in keywords:
        Q_objects |= Q(title__icontains=token)
        Q_objects |= Q(text__icontains=token)

    return Post.objects.filter(Q_objects)
