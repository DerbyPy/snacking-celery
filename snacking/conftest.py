import pytest

from snacking.celery.app import app, apply_config, create_config
import snacking.celery.testing as celery_testing


def pytest_configure(config):
    apply_config(app, '__tests__')


@pytest.fixture(scope='session')
def celery_config():
    """ Need to setup custom task annotations so the task tracker works correctly. """
    annotations = {'*': {'after_return': celery_testing.after_return_handler}}
    config = create_config('__tests__', task_annotations=annotations)
    return config
