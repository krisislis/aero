from dataclasses import asdict

from extractor import Extractor
from loader import Loader


class ELProcess:
    def __init__(self, extractor: Extractor, loader: Loader, data_model: type):
        self._extractor = extractor
        self._loader = loader
        self._data_model = data_model

    def run(self):
        data = self._extractor.extract()

        parsed_data = []

        for line in data:
            row = self._data_model(**line)
            parsed_row = []
            for col in self._data_model.get_columns():
                parsed_row.append(getattr(row, col))

            parsed_data.append(parsed_row)

        self._loader.load(parsed_data)
