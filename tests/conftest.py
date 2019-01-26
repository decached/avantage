import json
import logging
import os

import pytest

from avantage import Client

BASE_URI = 'https://www.alphavantage.co/query?datatype=json&apikey=demo&'
logging.getLogger().setLevel(logging.DEBUG)


@pytest.fixture
def sample_client():
    return Client(api_key='demo')


@pytest.fixture
def sample_params():
    return {'apikey': 'pytest', 'datatype': 'json'}


def mock_file(filename):
    cwd = os.path.dirname(__file__)
    with open(f'{cwd}/mocks/{filename}.json') as f:
        return json.loads(f.read())
