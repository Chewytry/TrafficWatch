from rest_framework import serializers
from .models import TrafficCamera

class TrafficCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficCamera
        fields = '__all__'
