import pytest
# this file also has to have the name `conftest.py`

from urlshort import create_app # This is the main function that still resides in the `__init__.py` file

@pytest.fixture # this is all predefined
def app():
    app = create_app() # exept for this
    yield app

@pytest.fixture # this is all predefined
def client(app):
    return app.test_client()