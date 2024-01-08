from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles, name='articles'),
    path('search/', views.articles, name='search'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('write/', views.write_article, name='write_article'),
]
