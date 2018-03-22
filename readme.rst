.. default-role:: code

Snacking on Celery's Readme
######################################

.. image:: https://circleci.com/gh/DerbyPy/snacking-celery.svg?style=shield
    :target: https://circleci.com/gh/DerbyPy/snacking-celery

.. image:: https://codecov.io/github/derbypy/snacking-celery/coverage.svg?branch=master&token=
    :target: https://codecov.io/github/derbypy/snacking-celery?branch=master

Introduction
=======================

You should be able to run the tests with::

    $ cd snacking-celery-src
    $ pipenv run tox


Or an app command like::

    $ pipenv run snacking hello


Running the celery worker::

    $ pipenv run celery -A snacking.celery.tasks worker --loglevel=info


Celery Resources
================

* `Celery: Getting Started <http://docs.celeryproject.org/en/latest/getting-started/index.html>`_
* `Celery: Using RabbitMQ <http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html>`_
* https://www.fullstackpython.com/task-queues.html
* https://www.rabbitmq.com/tutorials/tutorial-one-python.html


Alternatives
============

* https://kuyruk.readthedocs.io/en/latest/ (simple)
* https://huey.readthedocs.io/en/latest/ (Redis/SQLite only)
* http://python-rq.org/ (Redis only)
* https://github.com/closeio/tasktiger (Redis only)
* https://github.com/Bogdanp/dramatiq (be careful of the license:  Affero GPL)


Tutorial
========

* Hello

  * CLI
  * Worker

* RabbitMQ

  * Diagram
  * Worker output
  * Worker processes

    * 8
    * queue: snacking

* Flower?
