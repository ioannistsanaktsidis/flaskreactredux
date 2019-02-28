import pytest

from testapp import create_app, db


@pytest.fixture(scope='session')
def app():
    """Flask application fixture."""
    app_ = create_app()
    app_.config['SERVER_NAME'] = 'localhost:5000'
    app_.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    with app_.app_context():
        yield app_


@pytest.fixture(scope='function')
def isolated_app(app):
    db.create_all()
    yield app
    db.drop_all()
