import mock

from snacking.libs.testing import CLIBase


class TestUnit(CLIBase):

    def test_output(self):
        result = self.invoke('version')
        assert 'version' in result.output

    def test_hello_default(self):
        result = self.invoke('hello')
        assert 'Hello Celery Lovers!' in result.output

    def test_hello_argument(self):
        result = self.invoke('hello', 'Fred')
        assert 'Hello Fred!' in result.output

    def test_hello_task(self):
        # wrong approach
        # result = self.invoke('hello-task')
        # assert 'Hello Celery Lovers!' in result.output

        # correct approach
        with mock.patch('snacking.cli.tasks') as m_tasks:
            self.invoke('hello-task')
            m_tasks.hello.delay.assert_called_once_with('Celery Lovers')

        with mock.patch('snacking.cli.tasks') as m_tasks:
            self.invoke('hello-task', 'Foo')
            m_tasks.hello.delay.assert_called_once_with('Foo')
