# Flask-REST + WebUI
A Flask RESTful template for performing CRUD operations on an SQLAlchemy vehicle database.

### Configuration
* Create and load mariadb/mysql database from /dbinit
 

WebUI --> http://localhost:8080 --> REST <--> http://localhost:8088/api/asteroids

### Docker Notes:
```console
docker-compose up --build --force-recreate --no-deps [-d]

# Run APP with environment variables
docker run --env-file app/.env -p 8080:8080 fullaware/asteroid-app:latest

# Run API with environment variables
docker run --env-file api/.env -p 8088:8088 fullaware/asteroid-api:latest



# Stop remove all docker containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

SQLAlchemy used to execute following queries

Car Count
```sql
SELECT COUNT(*) AS `car_count` ​FROM `car_demo`;
```

Average Horsepower
```sql
SELECT AVG(`car_hp`) AS `AverageHP`​ FROM `car_demo`;
```

Top Colors
```sql
SELECT car_color, COUNT(`car_color`) AS `car_count` ​
FROM `car_demo` ​
GROUP BY `car_color` ​
ORDER BY `car_count` DESC;​
```

# NOTE: issue with mysql-connector
https://stackoverflow.com/questions/73244027/character-set-utf8-unsupported-in-python-mysql-connector
Set requirements.txt `mysql-connector-python==8.0.29` instead of latest which is `8.0.30`
