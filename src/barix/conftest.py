import gocept.testdb
import pkg_resources
import pytest


@pytest.fixture('function')
def database():
    """Create a database containing the tables."""
    db = gocept.testdb.MySQL(
        pkg_resources.resource_filename(
            'barix', '../../barix-db/database.sql'),
        prefix='barix')
    db.create()
    yield db
    db.drop()
