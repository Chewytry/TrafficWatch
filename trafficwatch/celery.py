""" 
To periodically fetch traffic camera information
"""

from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from celery.schedules import crontab
from django.conf import settings 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trafficwatch.settings')

app = Celery('trafficwatch') 
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'amqp://user:password@rabbitmq/'

app.conf.beat_schedule = {
    'fetch-traffic-images-every-half-minute': {
        'task': 'apps.traffic.tasks.fetch_traffic_data_task',
        'schedule': 30.0,  # executes every 30 seconds
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    logger.info(f'Request: {self.request!r}')