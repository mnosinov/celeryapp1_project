from time import sleep
from datetime import datetime
from django.core.mail import send_mail
from celeryapp.celery import app


@app.task
def hello_world():
    for i in range(3):
        sleep(2)   # delay for 10 seconds
        print('hello_world task' + str(i))
    print('Hello World')


@app.task
def send_email_task():
    for i in range(3):
        sleep(2)   # delay for 10 seconds
        print('send_email_task task' + str(i))
    send_mail('My Subject asdf' +
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Email body text text asdfasdf.',
              'celerysender@mail.com',
              ['mnosinov@gmail.com', 'bmaratovphoto@gmail.com'])
