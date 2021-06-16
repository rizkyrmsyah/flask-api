from config.database import MysqlConfig
from app import *
from db import db
import os

# Init App
app.config['SQLALCHEMY_DATABASE_URI'] = MysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# Run Server
if __name__ == '__main__':
    app.run(
        host = os.environ.get("APP_HOST"), 
        port = os.environ.get("APP_PORT"), 
        debug = os.environ.get("APP_DEBUG")
    )  