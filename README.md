# Sport Fair  
Sport fair database contains information of the athlete and the country they come from.  


#### Athlete Table
| AthleteID |       Name      | Gender | CountryID |  Sport   |
|:---------:|:---------------:|:------:|:---------:|:--------:|
|      1    |   Tyler Samuel  |  male  |     1     | Swimming |
#### Customer Table
| CountryID | CountryName | 
|:---------:|:-----------:|
|    1      |    Latvia   |

# Instructions  

### 1. Create sportfair.schema.
```
CREATE TABLE IF NOT EXISTS athlete (
    athlete_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255)    NOT NULL,
    gender varchar(255) NOT NULL,
    country_id    INTEGER DEFAULT 0,
    sport varchar(255) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);

CREATE TABLE IF NOT EXISTS country (
    country id             INTEGER PRIMARY KEY,
    country_name          varchar(255) NOT NULL
);
```
### 2. Create grocery_store.db.
```python
sqlite3 sportfair.db < sportfair.schema
```

### 3. Import the data from csv files to the database.
```python
sqlite> .mode csv
sqlite> .import data/AthleteData.csv athlete
sqlite> .import data/CountryData.csv country
```