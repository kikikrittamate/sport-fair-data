from models.country_models import CountryModel
from sqlalchemy.orm.session import Session


class CountryDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_country(self):
        return self.__session.query(CountryModel).all()

    def get_states_by_country_id(self, country_id):
        return self.__session.query(CountryModel).filter(CountryModel.country_id == country_id)[0]

    def get_states_by_country_name(self, country_name):
        return self.__session.query(CountryModel).filter(CountryModel.country_name == country_name).all()

    def add_country(self, country: CountryModel):
        self.__session.add(country)
        self.__session.commit()
        print("New country added.")