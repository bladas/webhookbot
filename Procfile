web: gunicorn pybot.wsgi --log-file -
celery: celery worker -A bladaswebhookbot -l info -c 4