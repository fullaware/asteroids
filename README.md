# Flask-REST + WebUI
Flask + REST + WebUI for performing CRUD operations on an SQLAlchemy asteroid database.

### Configuration
* Create and load mariadb/mysql database from /dbinit
* Update api/.env with proper mysql location for docker/local dev deployment
* Update app/.env with proper location of API Hostname

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

### Kubernetes Notes:
```console
kubectl apply -k kustomize/

```

# NOTE: issue with mysql-connector
https://stackoverflow.com/questions/73244027/character-set-utf8-unsupported-in-python-mysql-connector
Set requirements.txt `mysql-connector-python==8.0.29` instead of latest which is `8.0.30`


Can't parse 910000000000000000000 into sizekg even though this is how many kg Ceres is.
```
{"name": "1 Ceres", "sizekg": "910000000000000000000", "hazard": "N", "diameterkm": "939.4", "spectraltype": "C", "rotationh": "9.07417", "au": "1.59478"} 
```


### Design Notes:

|                                  |                       |
|----------------------------------|-----------------------|
| **Falcon 9 speed in kph**        | 28163.52              |
| **1 AU in km**                   | 149597870.7           |
| **Time to travel 1 AU in hours** | 5311.760416           |
| **Time to travel 1 AU in days**  | 221.3233507           |
| **Ceres size kg**                | 910000000000000000000 |
