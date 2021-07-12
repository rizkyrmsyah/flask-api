from config import http, configuration
from helpers.alchemy import sql_alchemy as db
from helpers.marshmallow import marshmallow as ma
import datetime

class UserActivity(db.Model):
    
    __tablename__ = 'user_activities'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    message = db.Column(db.TEXT())
    created_at = db.Column(db.DateTime(True), default=db.func.now())
    updated_at = db.Column(db.DateTime(True), default=db.func.now())

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message