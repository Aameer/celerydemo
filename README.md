#Celery as asynchronous task queue with rabbitmq as broker
celery docs:

Celery is an asynchronous task queue/job queue based on distributed message passing.    It is focused on real-time operation, but supports scheduling as well.The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet,  or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
Celery is used in production systems to process millions of tasks a day. (http://www.celeryproject.org/)



mkviretualenv celerydemo

start from here:
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#first-steps

In this tutorial you will learn the absolute basics of using Celery. You will learn about;

Choosing and installing a message transport (broker).
Installing Celery and creating your first task.
Starting the worker and calling tasks.
Keeping track of tasks as they transition through different states, and inspecting return values.

1.chosing a broker: rabbitmq as not negative mentioned
sudo apt-get install rabbitmq-server (https://www.rabbitmq.com/)


Installing celery:
pip install celery

Install django
pip install Django==1.7

mkdir celerydemo
cd celerydemo
django-admin startproject mysite
pwd > ~/.virtualenvs/celerydemo/.project

python manage.py migrate

python manage.py runserver


http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
pip install django-celery
Add djcelery to INSTALLED_APPS.
python manage.py migrate djcelery


inside the mysite/celery.py add some code for initializing celery
Also add in mysite/__init__
plus then we can have a demoapp whcih will have tasks.py file from where we can add tasks and import and call delay on them 



run the celery:
python manage.py celeryd -B -l info

run the camera
python manage.py celery events --camera=djcelery.snapshot.Camera

run the server:
python manage runserver

python manage shell
from demoapps.tasks import add
add.delay(4,4)

check the celery console to see the tasks






