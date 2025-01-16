from typing import Dict
from datetime import datetime, UTC
from pydantic import BaseModel, Field

class LegoSet(BaseModel):
    id: int
    name: str
    category_name: str
    pieces: int
    year: int
    weigh: float
    dimensions: dict
    ages: int
    minifigures: list
    images: list
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
