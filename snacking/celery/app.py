from celery import Celery


def create_config(queue_name, **kwargs):
    config = {
        # Celery does an `import` of these modules to make sure tasks are loaded
        'broker_url': 'pyamqp://guest@localhost//',
        'include': ['snacking.celery.tasks'],
        'task_default_queue': queue_name,
    }
    config.update(kwargs)
    return config


def apply_config(celery_app, queue_name='snacking'):
    celery_app.conf.update(create_config(queue_name))


app = Celery(__name__, )
