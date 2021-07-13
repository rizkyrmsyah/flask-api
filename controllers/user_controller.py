from flask import jsonify
from helpers.alchemy import sql_alchemy as db
from http import HTTPStatus
from datetime import datetime, timedelta
from helpers.jwt_helper import *
from helpers.bcrypt import bcrypt

from models import User, UserSchema, UserActivity


class UserController(object):
    @jwt_required()
    def show(self):
        user = User.query.filter_by(id=get_jwt_identity()).first()
        user_schema = UserSchema()
        data = user_schema.dump(user)

        # save user activity
        save_activity = UserActivity(user_id=user.id, message="Melihat profile")
        db.session.add(save_activity)
        db.session.commit()

        return jsonify(message="success", data=data)

    @jwt_required()
    def change_password(self, request: dict):
        user = User.query.filter_by(id=get_jwt_identity()).first()
        if not bcrypt.check_password_hash(user.password, request["old_password"]):
            return (
                jsonify(message="Kata sandi lama yang kamu masukkan salah"),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        password = bcrypt.generate_password_hash(request["password"])
        user.password = password
        user.updated_at = datetime.now()

        # save user activity
        save_activity = UserActivity(user_id=user.id, message="Merubah password")
        db.session.add(save_activity)
        db.session.commit()

        return jsonify(message="Ubah kata sandi berhasil")

    @jwt_required()
    def change_name(self, request: dict):
        user = User.query.filter_by(id=get_jwt_identity()).first()
        user.name = request["name"]
        user.updated_at = datetime.now()

        # save user activity
        save_activity = UserActivity(user_id=user.id, message="Merubah nama")
        db.session.add(save_activity)
        db.session.commit()

        return jsonify(message="Ubah nama berhasil")

    @jwt_required()
    def change_email(self, request: dict):
        user = User.query.filter(User.id == get_jwt_identity()).update(
            {User.email: request["email"], User.updated_at: datetime.now()}
        )

        # save user activity
        activity = UserActivity(user_id=get_jwt_identity(), message="Merubah email")
        db.session.add(activity)
        db.session.commit()

        return jsonify(message="ubah email berhasil")
