# replace 'proj' with the name of your django project.
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from botmodels.tasks import periodic_send
# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pybot.settings')

app = Celery('pybot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, periodic_send.s(), name='add every 60')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
