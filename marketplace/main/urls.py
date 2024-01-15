from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('explore/', views.explore, name='like'),
    path('api/', include(router.urls)),
]
