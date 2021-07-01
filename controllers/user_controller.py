from flask import jsonify
from helpers.alchemy import sql_alchemy as db
from models import User, UserSchema
from http import HTTPStatus
from datetime import datetime, timedelta
from helpers.jwt_helper import *
from helpers.bcrypt import bcrypt

class UserController(object):

    @jwt_required()
    def show(self):
        user = User.query.filter_by(id = get_jwt_identity()).first()
        user_schema = UserSchema()
        data = user_schema.dump(user)

        return jsonify(message = "success", data = data)
    
    @jwt_required()
    def change_password(self, request:dict):
        user = User.query.filter_by(id = get_jwt_identity()).first()
        if request['password'] != request['confirm_password']:
            return jsonify(message = "Password dan konfirmasi password tidak sama"), HTTPStatus.UNPROCESSABLE_ENTITY

        if not bcrypt.check_password_hash(user.password, request['old_password']):
            return jsonify(message = "Password lama salah"), HTTPStatus.UNPROCESSABLE_ENTITY

        password = bcrypt.generate_password_hash(request['password'])
        user.password = password
        user.updated_at = datetime.now()
        db.session.commit()

        return jsonify(message = "Ubah password berhasil")

    @jwt_required()
    def change_name(self, request:dict):
        user = User.query.filter_by(id = get_jwt_identity()).first()
        user.name = request['name']
        user.updated_at = datetime.now()
        db.session.commit()
        return jsonify(message = "Ubah nama berhasil")