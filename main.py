import settings
from el_process import ELProcess
from extractor import ApiExtractor
from loader import PostgresLoader
from model import CannabisModel

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
