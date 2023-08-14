import logging

import settings
from cannabis_el.el_process import ELProcess
from cannabis_el.extractor import ApiExtractor
from cannabis_el.loader import PostgresLoader
from cannabis_el.model import CannabisModel

logging.basicConfig(level=logging.INFO, filename='aero.log', filemode='w')

DB_PARAMS = {
    'dbname': settings.DB_NAME,
    'user': settings.DB_USER,
    'password': settings.DB_PASSWORD,
    'host': settings.DB_HOST
}

data_model = CannabisModel
table = 'staging.cannabis'

extractor = ApiExtractor(
    url='https://random-data-api.com/api/cannabis/random_cannabis?size=10',
    model=data_model,
)
loader = PostgresLoader(db_params=DB_PARAMS, table=table, columns=data_model.get_columns())
el_process = ELProcess(extractor=extractor, loader=loader)
el_process.run()
