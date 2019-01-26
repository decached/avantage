import json

import responses

from tests.conftest import mock_file, BASE_URI


@responses.activate
def test_quote(sample_client, sample_params):
    sample_params.update({'function': 'GLOBAL_QUOTE', 'symbol': 'MSFT'})
    want = mock_file('quote')
    responses.add(
        responses.GET,
        BASE_URI + 'function=GLOBAL_QUOTE&symbol=MSFT',
        status=200,
        body=json.dumps(want),
        match_querystring=True
    )
    got = sample_client.quote('MSFT')
    assert got == want['Global Quote']


@responses.activate
def test_search(sample_client, sample_params):
    sample_params.update({'function': 'SYMBOL_SEARCH', 'keywords': 'Micro'})
    want = mock_file('search')
    responses.add(
        responses.GET,
        BASE_URI + 'function=SYMBOL_SEARCH&keywords=Micro',
        status=200,
        body=json.dumps(want),
        match_querystring=True
    )
    got = sample_client.search('Micro')
    assert got == want['bestMatches']
