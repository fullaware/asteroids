FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=I@mR00t

COPY asteroids.sql /docker-entrypoint-initdb.d/
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf 
EXPOSE 3306
CMD [ "mysqld" ]