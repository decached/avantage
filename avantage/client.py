from logging import getLogger
from typing import Dict, List

import requests

__all__ = [
    'Client'
]


class Client:
    __logger__ = getLogger(__file__)

    def __init__(self, api_key: str):
        self.api_key = api_key

    def __get(self, payload: Dict) -> Dict:
        payload['apikey'] = self.api_key
        payload['datatype'] = 'json'

        response = requests.get('https://www.alphavantage.co/query', params=payload)
        return response.json()

    def quote(self, symbol: str) -> Dict:
        res_json = self.__get({'function': 'GLOBAL_QUOTE', 'symbol': symbol})
        return res_json['Global Quote']

    def search(self, keywords) -> List:
        response = self.__get({'function': 'SYMBOL_SEARCH', 'keywords': keywords})
        return response['bestMatches']
