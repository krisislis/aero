import abc

import psycopg2


class Loader(abc.ABC):
    @abc.abstractmethod
    def load(self, data):
        ...


class PostgresLoader(Loader):
    def __init__(self, db_params: dict, table: str, columns: list[str]):
        self.db_params = db_params
        self.table = table
        self.columns = columns
        values = ', '.join(['%s'] * len(self.columns))
        self.query = f'INSERT INTO {self.table}({",".join(self.columns)}) VALUES ({values})'

    def load(self, data):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.executemany(self.query, data)
                    conn.commit()
        except Exception as e:
            print(e)
            return []
