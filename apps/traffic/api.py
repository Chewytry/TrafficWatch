from __future__ import absolute_import, unicode_literals
import requests
import logging
from datetime import datetime
from celery import shared_task
from django.conf import settings
from .models import TrafficCamera
from trafficwatch.celery import app

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.task
def fetch_traffic_images():
    logging.info("Starting to fetch traffic camera images.")

    try:
        url = 'https://api.data.gov.sg/v1/transport/traffic-images'
        response = requests.get(url)
        data = response.json()
        for item in data['items']:
            for camera in item['cameras']:
                timestamp = datetime.fromisoformat(camera['timestamp'].rstrip('Z'))
                TrafficCamera.objects.update_or_create(
                    camera_id=camera['camera_id'],
                    defaults={
                        'latitude': camera['location']['latitude'],
                        'longitude': camera['location']['longitude'],
                        'image_url': camera['image'],
                        'timestamp': timestamp,
                        'image_height': camera['image_metadata']['height'],
                        'image_width': camera['image_metadata']['width'],
                        'image_md5': camera['image_metadata']['md5'],
                    }
                )
        logging.info("Successfully fetched and updated traffic camera images.")
    except Exception as e:
        logging.error(f"Error fetching traffic camera images: {e}")