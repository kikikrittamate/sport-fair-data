from utils.sport_fair import SportFair
from models.athlete_models import AthleteModel
from models.country_models import CountryModel

sport_fair = SportFair()

print(sport_fair.athlete().get_all_citizen())
print(sport_fair.athlete().get_citizen_by_athlete_id(67))
print(sport_fair.athlete().get_citizen_by_name("Liam Wise"))
print(sport_fair.athlete().get_citizen_by_country_id("24"))
print(sport_fair.athlete().get_citizen_by_sport("Swimming"))
print(sport_fair.country().get_all_states())
print(sport_fair.country().get_states_by_country_id(14))
print(sport_fair.country().get_states_by_country_name("Thailand"))

new_athlete = AthleteModel(athlete_id=101, name="Kiki Krub", gender="Male",
                           country_id=8, sport="Badminton")

new_country = CountryModel(country_id=51, country_name="new world")

sport_fair.athlete().add_athlete(new_athlete)
sport_fair.country().add_country(new_country)
