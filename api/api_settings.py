from flask import Flask, request, Response, jsonify
from flask_restful import reqparse, abort, Api, Resource
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

if "DB_SERVER" in os.environ and "DB_USER" in os.environ and "DB_PW" in os.environ:
    db_server = os.environ['DB_SERVER']
    db_username = os.environ['DB_USER']
    db_password = urllib.parse.quote_plus(os.environ['DB_PW']) # Fix for passwords with non-alphanumeric symbols
    db_name = os.environ['DB_NAME']
    
    print(f"Connecting to db server {db_server} on db {db_name}\n")
else:
    print(f"\nERROR : Missing environment variables:\n")
    print(f"DB_SERVER\nDB_USER\nDB_PW\nDB_NAME\n")
    print(f"Loading .env file...\n")

    db_server = os.getenv['DB_SERVER']
    db_username = os.getenv['DB_USER']
    db_password = urllib.parse.quote_plus(os.getenv['DB_PW']) # Fix for passwords with non-alphanumeric symbols
    db_name = os.getenv['DB_NAME']

# creating an instance of the flask app
app = Flask(__name__)
api = Api(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Configure our Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reader:Notr00t1@10.28.28.81:3306/car_demo'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_server}/{db_name}"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False