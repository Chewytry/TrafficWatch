from celery import shared_task
from trafficwatch.celery import app
from .api import fetch_traffic_images

@app.task()
def fetch_traffic_data_task():
    """ Periodically fetches traffic camera data """
    fetch_traffic_images()
