import click

@click.command()
@click.option('--width', default=720, type=int)
@click.option('--height', default=480, type=int)
@click.option('--n', default=50, type=int)
@click.option('--cycles', default=-1, type=int)
@click.pass_context
def cli(ctx: click.core.Context, width: int, height: int, n: int, cycles: int) -> None:
	pass