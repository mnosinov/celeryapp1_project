import os
import django

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp1_project.settings')
django.setup()

app = Celery('celeryapp')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-my-heart-beat-task-every-single-minute': {
        'task': 'celeryapp.tasks.heart_beat',
        'schedule': crontab(),
    },
    'run-my-15sec-beat-task-every-2mins': {
        'task': 'celeryapp.tasks.every_2mins_beat',
        'schedule': crontab(minute='*/2'),
    },
    #'sample_of_classbased_task_beat_that_runs_every_15mins': {
    #    'task': 'celeryapp.tasks.SomeClassBasedTask',
    #    'schedule': crontab(minute='*/15'),
    #},
}
