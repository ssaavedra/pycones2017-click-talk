import click

@click.command()
def cli():
    click.echo('This is a simple program created with Click.')

if __name__ == '__main__':
    cli()
