from __future__ import print_function

import datetime
import click

from snacking.celery.app import app, apply_config
from snacking.celery import tasks
from snacking.version import VERSION


def cli_entry():
    apply_config(app)
    snacking()


@click.group()
@click.pass_context
def snacking(ctx):
    pass


@snacking.command()
def version():
    click.echo('version: {}'.format(VERSION))


@snacking.command()
@click.argument('name', default='Celery Lovers')
def hello(name):
    tasks.hello(name)


@snacking.command('hello-task')
@click.argument('name', default='Celery Lovers')
def hello_task(name):
    tasks.hello.delay(name)
    print(datetime.datetime.now())


@snacking.command()
@click.argument('a', type=click.INT)
@click.argument('b', type=click.INT)
def add(a, b):
    tasks.add.delay(a, b)


@snacking.command()
def error():
    tasks.error.delay()


@snacking.command()
def retry():
    tasks.retry.delay()


@snacking.command()
@click.argument('queue_name', default='')
def purge(queue_name):
    if not queue_name:
        queue_name = app.conf['task_default_queue']

    with app.connection_for_write() as conn:
        conn.default_channel.queue_purge(queue_name)
    print('purged queue: {}'.format(queue_name))
