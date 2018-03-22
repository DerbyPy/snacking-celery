from snacking.libs.testing import CLIBase


class TestCLIUnit(CLIBase):

    def test_output(self):
        result = self.invoke('version')
        assert 'version' in result.output

    def test_hello_default(self):
        result = self.invoke('hello')
        assert 'Hello Celery Lovers!' in result.output

    def test_hello_argument(self):
        result = self.invoke('hello', 'Fred')
        assert 'Hello Fred!' in result.output
