import click
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image

@click.command()
@click.option('--message', '-m', default='LGTM')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM IMAGE GEN TOOL"""
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)