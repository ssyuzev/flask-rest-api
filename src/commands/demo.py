
import click
from flask.cli import with_appcontext


@click.command("say_hello")
@click.argument("name", required=False)
@with_appcontext
def cli_hello(name):
    """Demo cli function."""
    name = name if name else ""
    print(f"Hello {name}!")
