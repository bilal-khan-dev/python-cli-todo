"""tests"""
# test/test_mytodo.py

from typer.testing import CliRunner
from mylib import cli, __app_name__, __version__

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"Our awesome {__app_name__} CLI app with version {__version__}\n" in result.stdout
