import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Board.settings')

app = Celery('Board',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379',
             broker_connection_retry=False,
             broker_connection_retry_on_startup=True,
             broker_connection_max_retries=10,
             )
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'send_all_week_posts_every_monday_8am': {
        'task': 'adboard.tasks.all_week_posts',
        'schedule': crontab(hour='20', minute='30', day_of_week='monday'),  # частота выполнения
        'args': (),
    },
}  # а оно мне надо вообще

