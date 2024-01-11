from django.urls import path

from . import views

app_name = 'profiling'

urlpatterns = [
    path('<slug:author_username>/', views.profile, name='profile'),
    path('collection/<slug:collection_slug>/', views.collection, name='collection'),
    path('item/<int:id>/', views.item, name='item'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('create/', views.create_options, name='create_options'),
    path('create/single/', views.create_single, name='create_single'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('edit/item<int:id>/', views.edit_item, name='edit_item'),
    path('edit/delete<int:id>/', views.delete_item, name='delete_item')
]
