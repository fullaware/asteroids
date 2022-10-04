FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=I@mR00t
ENV MYSQL_DATABASE=car_demo

COPY car_demo.sql /docker-entrypoint-initdb.d/
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf 
EXPOSE 3306
CMD [ "mysqld" ]