# replace 'proj' with the name of your django project.
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pybot.settings')

app = Celery('pybot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-minute': {
        'task': 'botmodels.tasks.periodic_send',
        'schedule': crontab(minute=1),
        'args':"",
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
