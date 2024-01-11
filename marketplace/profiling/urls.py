from django.urls import path

from . import views

app_name = 'profiling'

urlpatterns = [
    path('collection/<slug:collection_slug>/', views.collection, name='collection'),
    path('item/<int:id>/', views.item, name='item'),


    path('create/', views.create_options, name='create_options'),
    path('create/single/', views.create_single, name='create_single'),

    path('edit/item<int:id>/', views.edit_item, name='edit_item'),
    path('edit/delete<int:id>/', views.delete_item, name='delete_item')
]
