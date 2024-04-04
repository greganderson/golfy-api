from uuid import UUID

from pydantic import BaseModel


class Player(BaseModel):
    id: UUID
    name: str
    handicap: float