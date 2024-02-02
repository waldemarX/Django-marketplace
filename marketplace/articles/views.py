from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone

from .utils import q_search
from .models import Post, Categories
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArticleCreationForm


def articles(request):
    template = "articles/articles.html"
    page = request.GET.get("page", 1)
    filter_category = request.GET.get("category", None)
    query = request.GET.get("q", None)

    if filter_category:
        posts = (
            Post.objects.select_related("category")
            .filter(is_published=True, category__slug=filter_category)
            .order_by("-pub_date")
        )
    elif query:
        posts = q_search(query)
    else:
        posts = (
            Post.objects.select_related("category")
            .filter(is_published=True)
            .order_by("-pub_date")
        )

    paginator = Paginator(posts, per_page=6)
    current_page = paginator.page(page)

    context = {
        "posts": current_page,
        "subtitle": "Articles",
        "dark": True,
    }
    return render(request, template, context)


def article_detail(request, article_id):
    template = "articles/article-detail.html"
    post_details = Post.objects.select_related("author").get(pk=article_id)
    context = {"post": post_details, "subtitle": post_details.title, "dark": True}
    return render(request, template, context)


@login_required
def write_article(request):
    template = "articles/write-article.html"

    categories = Categories.objects.all()

    if request.method == "POST":
        form = ArticleCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            category_name = request.POST["category"]
            category = Categories.objects.get(category_name=category_name)
            post.category = category
            post.save()
            messages.success(request, "Article successfully created!")
            return HttpResponseRedirect(reverse("articles:articles"))
        else:
            errors = {
                "Title": request.POST["title"],
                "Text": request.POST["text"],
                "Category": request.POST["category"],
            }
            errors = [err[0] for err in errors.items() if not err[1]]
            messages.error(
                request,
                f"Please, do not leave required fields blank -> {', '.join(errors)}",
            )

    else:
        form = ArticleCreationForm()

    date = timezone.now()
    context = {
        "categories": categories,
        "subtitle": "Write your article",
        "date": date,
        "dark": True,
    }
    return render(request, template, context)
