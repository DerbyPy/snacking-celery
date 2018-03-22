import pytest

from snacking.celery.app import create_config
import snacking.celery.testing as celery_testing


@pytest.fixture(scope='session')
def celery_config():
    """ Need to setup custom task annotations so the task tracker works correctly. """
    annotations = {'*': {'after_return': celery_testing.after_return_handler}}
    return create_config('__tests__', task_annotations=annotations)
