from django.urls import path
from .views import traffic_camera_list

urlpatterns = [
    path('cameras/', traffic_camera_list, name='camera-list'),
]
