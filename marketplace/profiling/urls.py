from django.urls import path

from . import views

app_name = 'profiling'

urlpatterns = [
    path('profile/1', views.profile, name='profile'),
    path('collection/1', views.collection, name='collection'),
    path('item/1', views.item, name='item')
]
