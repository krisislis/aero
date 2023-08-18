from pydantic import BaseModel


class Model(BaseModel):
    @classmethod
    def get_columns(cls) -> list[str]:
        ...
