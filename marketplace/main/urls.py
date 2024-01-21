from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'events', views.EventsViewSet)

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('like/', views.like, name='like'),
    path('explore/', views.explore, name='explore'),
    path('api/', include(router.urls)),
]
