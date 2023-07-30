FROM python:3.11-slim-bookworm 
RUN mkdir /my_flask_app
WORKDIR /my_flask_app
COPY requirements.txt /my_flask_app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY api/. /my_flask_app
EXPOSE 8088
ENTRYPOINT [ "gunicorn", "-b :8088", "api:app", "--log-file=-","--reload","--access-logfile=-", "--workers=2" ,"--threads=4", "--worker-class=gthread" ]
