import click

@click.command()
@click.option('--message', '-m', default='LGTM')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM IMAGE GEN TOOL"""
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm(keyword, message):
    pass