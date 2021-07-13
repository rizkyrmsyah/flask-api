from config import http, configuration
from helpers.alchemy import sql_alchemy as db
from helpers.marshmallow import marshmallow as ma
from helpers.jwt_helper import jwt_manager as jwt
import datetime


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email_verified_at = db.Column(db.DateTime(True))
    created_at = db.Column(db.DateTime(True), default=db.func.now())
    updated_at = db.Column(db.DateTime(True), default=db.func.now())

    def __init__(self, name, email, password, email_verified_at):
        self.name = name
        self.email = email
        self.password = password
        self.email_verified_at = email_verified_at

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "email",
            "email_verified_at",
            "created_at",
            "updated_at",
        )
        model = User
