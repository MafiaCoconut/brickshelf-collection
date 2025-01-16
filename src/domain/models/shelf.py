from datetime import datetime

from pydantic import BaseModel, Field

from src.domain.models.legoset import LegoSet


class Shelf(BaseModel):
    id: int
    author_id: int
    legosets: list[LegoSet]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
