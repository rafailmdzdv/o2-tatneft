from pydantic import BaseModel


class Card(BaseModel):

    id: int
    number: str
