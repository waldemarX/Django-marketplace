from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('api/itemlist', views.ItemApi.as_view(), name='itemlist'),
]
