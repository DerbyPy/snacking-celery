from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.conf.update({
    'task_default_queue': 'snacking',
})


@app.task
def hello(name):
    print('Hello {}!'.format(name))


@app.task
def add(x, y):
    return x + y


@app.task
def error():
    raise Exception('deliberate error for testing purposes')
