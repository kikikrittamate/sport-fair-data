from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AthleteModel(Base):
    __tablename__ = "athlete"

    athlete_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    country_id = Column(Integer, nullable=False)
    sport = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Athlete: (id={self.country_id},name={self.name},gender={self.gender}" \
               f",country_id={self.country_id},sport={self.sport})>"
