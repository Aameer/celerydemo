#celery.py
from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from django.conf import settings  # noqa
app = Celery('tasks', broker='amqp://guest@localhost//')

#app.conf.update(
#    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
#    CELERY_ACCEPT_CONTENT = ['json'],
#    CELERY_TASK_SERIALIZER = 'json',
#    CELERY_RESULT_SERIALIZER = 'json',
#)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
)

#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))

@app.task
def add(x, y):
    return x + y

