import click

@click.command()
@click.option('--width', default=720, type=int)
@click.option('--height', default=480, type=int)
@click.option('--n', default=50, type=int)
@click.option('--cycles', default=-1, type=int)
def cli(width: int, height: int, num_boids: int, cycles: int) -> None:
    print(width, height, num_boids, cycles)
