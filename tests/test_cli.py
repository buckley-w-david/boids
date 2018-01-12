from click.testing import CliRunner
from boids.cli import cli

def test_cli() -> None:
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
