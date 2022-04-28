from models.athlete_models import AthleteModels
from sqlalchemy.orm.session import Session


class AthleteDao:

    def __init__(self, session: Session):
        self.__session = session

    def get_all_athlete(self):
        return self.__session.query(AthleteModels).all()

    def get_athlete_by_athlete_id(self, athlete_id):
        return self.__session.query(AthleteModels).filter(AthleteModels.athlete_id == athlete_id)[0]

    def get_athlete_by_name(self, name):
        return self.__session.query(AthleteModels).filter(AthleteModels.name == name).all()

    def get_athlete_by_gender(self, gender):
        return self.__session.query(AthleteModels).filter(AthleteModels.gender == gender).all()

    def get_athlete_by_country_id(self, country_id):
        return self.__session.query(AthleteModels).filter(AthleteModels.country_id == country_id).all()

    def get_athlete_by_sport(self, sport):
        return self.__session.query(AthleteModels).filter(AthleteModels.sport == sport).all()

    def add_athlete(self, athlete: AthleteModels):
        self.__session.add(athlete)
        self.__session.commit()
        print("New athlete added.")
