from cannabis_el.extractor import Extractor
from cannabis_el.loader import Loader


class ELProcess:
    def __init__(self, extractor: Extractor, loader: Loader):
        self._extractor = extractor
        self._loader = loader

    def run(self):
        data = self._extractor.extract()
        self._loader.load(data)
