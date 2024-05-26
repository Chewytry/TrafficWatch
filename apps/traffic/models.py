from django.db import models

class TrafficCamera(models.Model):
    camera_id = models.CharField(max_length=20, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image_url = models.URLField(max_length=200)
    timestamp = models.DateTimeField()
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    image_md5 = models.CharField(max_length=32)

    def __str__(self):
        return f"Camera {self.camera_id} at {self.timestamp}"
