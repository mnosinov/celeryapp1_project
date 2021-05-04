from time import sleep
from datetime import datetime
from django.core.mail import send_mail
from celery import Task

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


class AuthTask(Task):
    name = "AuthTask"

    def __init__(self):
        self.auth_counter = 0
        self.users = {
            'user1': 'user11',
            'user2': 'user22',
        }

    def run(self, username, password):
        try:
            self.auth_counter += 1
            auth_result = self.users[username] == password
        except KeyError:
            auth_result = False
        return {
            "auth_result": auth_result,
            "auth_counter": self.auth_counter,
        }

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # here you can do some necessary actions
        # but they won't be applied to celery task processing
        # in celery it will be marked as FAILURE
        some_failure_data = {
            "my_message": "error has happened",
            "exc": exc,
            "task_id": task_id,
            "einfo": einfo,
        }
        print(some_failure_data)


class AddTask(Task):
    name = "AddTask"

    def run(self, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        sleep(4)
        return num1 + num2


app.tasks.register(AuthTask())
app.tasks.register(AddTask())
