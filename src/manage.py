#!/usr/bin/env python3

from flask.cli import FlaskGroup

from main import app
from commands.demo import cli_hello
from commands.db import reset_db, seed_db


cli = FlaskGroup(app)


cli.add_command(reset_db)
cli.add_command(seed_db)
cli.add_command(cli_hello)


if __name__ == "__main__":
    cli()
