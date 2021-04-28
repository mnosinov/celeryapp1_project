from time import sleep
from celeryapp.celery import app


@app.task
def hello_world():
    for i in range(5):
        sleep(2)   # delay for 10 seconds
        print(i)
    print('Hello World')
