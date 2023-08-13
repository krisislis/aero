import abc
from typing import Iterable

import requests


class Extractor(abc.ABC):
    @abc.abstractmethod
    def extract(self) -> Iterable:
        ...


class ApiExtractor(Extractor):
    def __init__(self, url: str):
        self.url = url

    def extract(self) -> Iterable:
        try:
            res = requests.get(self.url)
        except Exception as e:
            print(e)
            return []

        if res.status_code != 200:
            print('error')
            return []

        return res.json()
