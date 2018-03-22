import logging
import random

from .app import app

log = logging.getLogger(__name__)


@app.task
def hello(name):
    print('Hello {}!'.format(name))


@app.task
def add(x, y):
    return x + y


@app.task
def error():
    raise Exception('deliberate error for testing purposes')


@app.task(bind=True)
def retry(self, retry_wait_secs=0.25, max_retries=50):
    try:
        assert random.randint(1, 10) == 5
    except AssertionError as e:
        log.error('random int wasn\'t 5')
        self.retry(exc=e, countdown=retry_wait_secs, max_retries=max_retries)

    log.info('retry worked')
