import logging

from settings import SETTINGS
from core.el_process import ELProcess
from core.extractor import ApiExtractor
from core.loader import PostgresLoader
from core.model import Model

logging.basicConfig(level=logging.INFO, filename='logs/aero.log', filemode='w')

DB_PARAMS = {
    'dbname': SETTINGS['DB_NAME'],
    'user': SETTINGS['DB_USER'],
    'password': SETTINGS['DB_PASSWORD'],
    'host': SETTINGS['DB_HOST'],
}


class CannabisModel(Model):
    id: int
    uid: str
    strain: str
    cannabinoid_abbreviation: str
    cannabinoid: str
    terpene: str
    medical_use: str
    health_benefit: str
    category: str
    type: str
    buzzword: str
    brand: str

    @classmethod
    def get_columns(cls) -> list[str]:
        return [
            'id', 'uid', 'strain',
            'cannabinoid_abbreviation',
            'cannabinoid', 'terpene', 'medical_use',
            'health_benefit', 'category', 'type',
            'buzzword', 'brand',
        ]


def run():
    data_model = CannabisModel
    table = 'staging.cannabis'

    extractor = ApiExtractor(
        url='https://random-data-api.com/api/cannabis/random_cannabis?size=10',
        model=data_model,
    )
    loader = PostgresLoader(db_params=DB_PARAMS, table=table, columns=data_model.get_columns())
    el_process = ELProcess(extractor=extractor, loader=loader)
    el_process.run()


run()
