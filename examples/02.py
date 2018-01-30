import click

@click.command()
@click.option('--name', '-n',
	      default='world',
	      help='The name you want to greet')
def cli(name):
    click.echo('Hello, %s' % name)

if __name__ == '__main__':
    cli()
