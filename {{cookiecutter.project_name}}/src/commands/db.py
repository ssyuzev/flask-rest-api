import click

from flask.cli import with_appcontext

from models import db, User


@click.command("reset_db")
@with_appcontext
def reset_db():
    """Remove all data from DB."""
    print("Reset db...")
    db.drop_all()
    db.create_all()
    db.session.commit()


@click.command("seed_db")
@with_appcontext
def seed_db():
    """Populate Db with demo data."""
    print("Seed...")
    for i in range(8):
        db.session.add(
            User(
                email=f"test{i}@local.dev",
                password=f"MySecretPass00{i}",
                full_name=f"Demo User #00{i}",
            )
        )
        db.session.commit()
