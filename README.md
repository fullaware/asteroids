# Flask-REST + WebUI
Flask + REST + WebUI for performing CRUD operations on an SQLAlchemy asteroid database.

### Configuration
* Create and load mariadb/mysql database from /dbinit
 

WebUI --> http://localhost:8080 --> REST <--> http://localhost:8088/api/asteroids <--> MariaDB/MySQL

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

# NOTE: issue with mysql-connector
https://stackoverflow.com/questions/73244027/character-set-utf8-unsupported-in-python-mysql-connector
Set requirements.txt `mysql-connector-python==8.0.29` instead of latest which is `8.0.30`
