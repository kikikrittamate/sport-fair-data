from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.athlete_dao import AthleteDao
from utils.dao.country_dao import CountryDao


class SportFair:

  def __init__(self, connection_url="sqlite:///sportfair.db"):
    engine = create_engine(connection_url)
    session = sessionmaker(bind=engine)
    self.__db_session = session()

  def athlete(self):
    return AthleteDao(self.__db_session)

  def country(self):
    return CountryDao(self.__db_session)
