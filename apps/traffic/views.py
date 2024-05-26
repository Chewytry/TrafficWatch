from django.http import JsonResponse
from .models import TrafficCamera

def traffic_camera_list(request):
    cameras = TrafficCamera.objects.all()
    data = [{
        "camera_id": cam.camera_id, 
        "image_url": cam.image_url, 
        "timestamp": cam.timestamp.isoformat(), 
        "latitude": cam.latitude, 
        "longitude": cam.longitude
        } for cam in cameras]
    return JsonResponse(data, safe=False)
