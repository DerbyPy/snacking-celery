import mock
import pytest

from snacking.celery import tasks


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
