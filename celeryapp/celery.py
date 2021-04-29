import os
import django

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp1_project.settings')
django.setup()

app = Celery('myceleryapp')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'run-every-single-minute': {
        'task': 'celeryapp.tasks.heart_beat',
        'schedule': crontab(),
    },
}
