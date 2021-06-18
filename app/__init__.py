from flask import Flask
from config.database import MysqlConfig
from db import db
import os

# Init App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = MysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = os.environ.get("APP_KEY")
db.init_app(app)

from app.controller import  *