import abc
import logging
from typing import Iterable

import psycopg2

from cannabis_el.model import Model


class Loader(abc.ABC):
    @abc.abstractmethod
    def load(self, data: Iterable[Model]) -> None:
        ...


class PostgresLoader(Loader):
    def __init__(self, db_params: dict, table: str, columns: list[str]):
        self.db_params = db_params
        self.table = table
        self.columns = columns
        values = ', '.join(['%s'] * len(self.columns))
        self.query = f'INSERT INTO {self.table}({",".join(self.columns)}) VALUES ({values})'

    def load(self, data: Iterable[Model]) -> None:
        parsed_data = []

        for line in data:
            parsed_row = []
            for col in self.columns:
                parsed_row.append(getattr(line, col))
            parsed_data.append(parsed_row)

        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.executemany(self.query, parsed_data)
                    conn.commit()
        except Exception as e:
            logging.error('Fail to load data into database', e)
