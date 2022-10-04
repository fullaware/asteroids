FROM python:3.10-slim-bullseye
RUN mkdir /my_flask_app
WORKDIR /my_flask_app
COPY requirements.txt /my_flask_app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY api/. /my_flask_app
EXPOSE 8088
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]
