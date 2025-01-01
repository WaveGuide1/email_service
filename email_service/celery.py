import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.settings')
celery_app = Celery('email_service')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()