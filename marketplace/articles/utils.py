from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from .models import Post

# from django.db.models import Q


def q_search(query):
    vector = SearchVector("title", "text")
    query = SearchQuery(query)
    result = (
        Post.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result = result.annotate(
        headline=SearchHeadline(
            "title",
            query,
            start_sel='<span class="NoClass" style="background-color: orange;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "text",
            query,
            start_sel='<span class="NoClass" style="font-weight: bold;">',
            stop_sel="</span>",
            max_fragments=1,
        )
    )
    return result

    # lite version

    # keywords = [word for word in query.split() if len(word) > 1]

    # Q_objects = Q()

    # for token in keywords:
    #     Q_objects |= Q(title__icontains=token)
    #     Q_objects |= Q(text__icontains=token)

    # return Post.objects.filter(Q_objects)
