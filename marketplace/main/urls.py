from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/like/', views.like, name='like'),
    path('api/check_if_like/', views.check_if_like, name='check_if_like'),
]
