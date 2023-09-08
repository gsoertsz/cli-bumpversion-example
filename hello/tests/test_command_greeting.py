import pytest
from hello.hello import say_hello
from click.testing import CliRunner
from datetime import datetime

from mock import patch

def test_command_get_result():
    with patch('hello.greeting.greeting.generate') as generate_mock:

        runner = CliRunner()

        generate_mock.return_value = 'Hello Billy, Goodbye'

        result = runner.invoke(say_hello, ['--to-whom', 'Billy', '--greeting', 'Goodbye'])
        
        assert result.exit_code == 0
        assert generate_mock.call_count == 1
        assert result.output == 'Hello Billy, Goodbye\n'
