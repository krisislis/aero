from pydantic import BaseModel


class Model(BaseModel):
    @classmethod
    def get_columns(cls) -> list[str]:
        ...


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
