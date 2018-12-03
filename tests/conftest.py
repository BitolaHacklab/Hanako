import os
import tempfile

import pytest

from hanako.cli import server


@pytest.fixture
def client():
    db_fd, server.api.config['DATABASE'] = tempfile.mkstemp()
    server.api.config['TESTING'] = True
    client = server.api.test_client()

    # when we have DATABASE
    #with server.api.app_context():
        #server.init_db()

    yield client

    os.close(db_fd)
    os.unlink(server.api.config['DATABASE'])
