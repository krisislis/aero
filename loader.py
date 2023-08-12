import psycopg2 as psycopg2
import requests

DB_PARAMS = {
    'dbname': 'cannabis',
    'user': 'postgres',
    'password': 'postgres',
    'host': '127.0.0.1'
}


def extract_raw_data(size: int = 10):
    try:
        res = requests.get(f'https://random-data-api.com/api/cannabis/random_cannabis?size={size}')
    except Exception as e:
        return []

    if res.status_code != 200:
        return []

    return res.json()


def insert_data(table, columns, data: list[list]):
    values = ', '.join(['%s'] * len(columns))
    query = f'INSERT INTO {table}({",".join(columns)}) VALUES ({values})'
    try:
        with psycopg2.connect(**DB_PARAMS) as conn:
            with conn.cursor() as cur:
                cur.executemany(query, data)
                conn.commit()
    except Exception as e:
        print(e)
        return []


def save_data(data: list[dict]):
    table = 'staging.cannabis'
    columns = (
        'id', 'uid', 'strain',
        'cannabinoid_abbreviation',
        'cannabinoid', 'terpene', 'medical_use',
        'health_benefit', 'category', 'type',
        'buzzword', 'brand',
    )
    parsed_data = []

    for line in data:
        row = []
        for c in columns:
            row.append(line.get(c))
        parsed_data.append(row)

    insert_data(table, columns, parsed_data)


data = extract_raw_data()
save_data(data)
