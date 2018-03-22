import mock
import pytest

from snacking.celery import tasks
from snacking.celery.testing import task_tracker


class TestTasksUnit:

    @mock.patch.object(tasks, 'print')
    def test_hello(self, m_print):
        tasks.hello('foobar')
        m_print.assert_called_once_with('Hello foobar!')

    def test_add(self):
        assert tasks.add(2, 3) == 5

    def test_error(self):
        with pytest.raises(Exception) as excinfo:
            assert tasks.error()
        assert str(excinfo.value) == 'deliberate error for testing purposes'


class TestTasksIntegration:

    def setup(self):
        task_tracker.reset()

    @mock.patch.object(tasks, 'log')
    def test_retry(self, m_log, celery_session_worker):

        tasks.retry.delay()

        result = task_tracker.wait_for('snacking.celery.tasks.retry')
        assert result.status == 'SUCCESS', result

        m_log.info.assert_called_once_with('retry worked')
