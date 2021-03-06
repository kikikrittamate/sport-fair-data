from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import decl_base

Base = decl_base()


class CountryModels(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, nullable=False)
    country_name = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Country: (country id={self.country_id},country name={self.country_name})>"
