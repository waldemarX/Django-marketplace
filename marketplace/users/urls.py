from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('wallet/', views.wallet, name='wallet'),
    path('<slug:author_username>/', views.profile, name='profile'),

]
