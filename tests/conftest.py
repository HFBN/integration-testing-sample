import pytest

from api.app import create_app
from api.config import Config

@pytest.fixture(scope='session')
def app():
    app = create_app(config_object=Config())
    # app = app.app
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client