import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.task_default_queue = 'default'

app.conf.beat_schedule = {
    'delete_old_urls': {
        'task': 'shortener.tasks.delete_old_urls',
        'schedule': crontab(minute=0, hour=0),
    },
}
