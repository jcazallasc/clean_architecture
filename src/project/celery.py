import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

redis_host = os.getenv("REDIS_HOST")
redis_db = os.getenv("REDIS_DB")

app = Celery('events', broker=f'redis://{redis_host}/{redis_db}')

app.autodiscover_tasks([
    'janto_events_context.infrastructure',
])
