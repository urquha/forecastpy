from typing import Dict, Optional
from timeit import default_timer as timer

import requests
import requests_cache



class Requestor:

    def __init__(self, account_id, auth_token, cache, base_url=None):
        self._account_id = account_id
        self._auth_token = auth_token
        self.cache = cache
        if cache:
            print("Adding cache")
            requests_cache.install_cache(cache_name='forecast_cache', backend='sqlite', expire_after=180)
        if base_url is None:
            self._base_url = "https://api.forecastapp.com"

        self._headers = {
            'Forecast-Account-ID': self._account_id,
            'Authorization': 'Bearer {}'.format(self._auth_token),
            'User-Agent': 'Forecast Harvest Python API',
        }


    def get(self, endpoint: str) -> Dict:
        start = timer()
        r = requests.get("{}/{}".format(self._base_url, endpoint), headers=self._headers)
        end = timer()
        if self.cache:
            print("Enpoint: {0} | Time: {1} | Cache: {2}".format(endpoint, end - start, r.from_cache, ))
        else:
            print("Enpoint: {0} | Time: {1} ".format(endpoint, end - start ))
        return r.json()

    @staticmethod
    def clear_cache(self):
        if self.cache:
            requests_cache.clear()
