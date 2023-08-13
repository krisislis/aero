import abc
from typing import Iterable

import requests

from model import Model


class Extractor(abc.ABC):
    @abc.abstractmethod
    def extract(self) -> Iterable[Model]:
        ...


class ApiExtractor(Extractor):
    def __init__(self, url: str, model: type):
        self.url = url
        self.model = model

    def extract(self) -> Iterable[Model]:
        try:
            res = requests.get(self.url)
        except Exception as e:
            print(e)
            return []

        if res.status_code != 200:
            print('error')
            return []

        return [self.model(**elem) for elem in res.json()]
