import click

from flask.cli import with_appcontext

from testapp import db


@click.group('db')
def db_cli():
    """Command to perform db actions"""


@db_cli.command('create')
@with_appcontext
def db_create():
    """Initializes the db."""
    try:
        db.create_all()
        click.echo(click.style('Database successfully initialized.',
                               fg='green'))
    except Exception as e:
        click.echo(
            click.style(
                'Something went wrong while creating the database:\n{0}'
                .format(e), fg='red'), err=True)


@db_cli.command('drop')
@with_appcontext
def db_drop():
    """Drops the db."""
    try:
        db.drop_all()
        click.echo(click.style('Database successfully dropped.',
                               fg='green'))
    except Exception as e:
        click.echo(
            click.style(
                'Something went wrong while dropping the database:\n{0}'
                .format(e), fg='red'), err=True)
