from __future__ import print_function

import datetime
import click

from snacking.celery import tasks
from snacking.version import VERSION


def cli_entry():
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
@click.argument('name', default='World')
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
