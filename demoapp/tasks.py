from __future__ import absolute_import

from celery import shared_task,task

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task()
#@task(name='demoapp.tasks.add')
def add(x, y):
    print(x,y)
    logger.debug('Adding %r + %r' % (x, y))
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
