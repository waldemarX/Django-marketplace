from .models import Post


def q_search(query):
    if query.isdigit():
        return Post.objects.select_related('category').filter(id=int(query), is_published=True).order_by('-pub_date')
