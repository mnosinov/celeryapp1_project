from time import sleep
from datetime import datetime
from django.core.mail import send_mail
from celeryapp.celery import app


@app.task
def show_index_task():
    sleep(6)
    print('Index page has been shown 2 seconds ago. ')


@app.task
def hello_world_task(name):
    for i in range(3):
        sleep(2)   # delay for 10 seconds
        print('hello_world task' + str(i))
    hello_phrase = 'Hello ' + name
    print(hello_phrase)
    return hello_phrase


@app.task
def send_email_task():
    for i in range(3):
        sleep(2)   # delay for 10 seconds
        print('send_email_task task' + str(i))
    send_mail('My Subject asdf' +
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Email body text text asdfasdf.',
              'celerysender@mail.com',
              ['mnosinov@gmail.com', 'bmaratovphoto@gmail.com'])


@app.task
def heart_beat():
    print('Heart Beat! now is ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.task
def every_2mins_beat():
    print('Every 2 minutes Beat! ' + datetime.now().strftime('%H:%M:%S'))
    return 'My Result is: ' + 'Every 2 minutes Beat! ' + datetime.now().strftime('%H:%M:%S')
