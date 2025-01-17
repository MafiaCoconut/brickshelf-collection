from datetime import datetime

from sqlalchemy import Column, String, JSON, Integer, Float, text,
from sqlalchemy.orm import Mapped, mapped_column
#
# from infrastructure.db.base import Base
#
#
class LegoSetOrm(Base):
    __tablename__ = "legosets"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, default="-")
    category_name: Mapped[str] = mapped_column(String, default="-")
    pieces: Mapped[int] = mapped_column(Integer, default=0)
    year: Mapped[int] = mapped_column(Integer, default=0)
    weigh: Mapped[float] = mapped_column(Float, default=0.0)
    dimensions: Mapped[dict] = mapped_column(JSON, default={})
    ages: Mapped[int] = mapped_column(Integer, default=0)
    minifigures: Mapped[list] = mapped_column(List, default=[])
    images: Mapped[list] = mapped_column(List, default=[])
    description: Mapped[str] = mapped_column(String, default="-")
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

