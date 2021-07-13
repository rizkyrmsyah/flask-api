from flask import jsonify
from helpers.alchemy import sql_alchemy as db
from helpers.bcrypt import bcrypt
from http import HTTPStatus
from datetime import datetime, timedelta
from helpers.jwt_helper import *

from models import User, UserActivity


class SessionController(object):
    def register(self, request: dict):
        try:
            # generate password and save request to database
            password = bcrypt.generate_password_hash(request["password"])
            save_user = User(
                email=request["email"],
                password=password,
                name=request["name"],
                email_verified_at=None,
            )
            db.session.add(save_user)
            db.session.flush()

            # save user activity
            save_activity = UserActivity(user_id=save_user.id, message="Bergabung")
            db.session.add(save_activity)

            # generate access token
            access_token = create_access_token(
                identity=save_user.id, expires_delta=timedelta(days=1)
            )

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return (
                jsonify(message="Terjadi kesalahan pada sistem : " + str(e)),
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )

        return (
            jsonify(message="Registrasi berhasil", access_token=access_token),
            HTTPStatus.CREATED,
        )

    def login(self, request: dict):
        user = User.query.filter_by(email=request["email"]).first()
        if user is None or not bcrypt.check_password_hash(
            user.password, request["password"]
        ):
            return (
                jsonify(
                    message="Kami tidak bisa menemukan akun yang cocok dengan data yang kamu masukkan. Harap periksa kembali dan coba lagi."
                ),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        # save user activity
        save_activity = UserActivity(user_id=user.id, message="Melakukan login")
        db.session.add(save_activity)
        db.session.commit()

        # generate access token
        access_token = create_access_token(
            identity=user.id, expires_delta=timedelta(days=1)
        )

        return jsonify(message="success", access_token=access_token)

    @jwt_required()
    def check_password(self, request: dict):
        user = User.query.filter_by(id=get_jwt_identity()).first()
        if user is None or not bcrypt.check_password_hash(
            user.password, request["password"]
        ):
            return (
                jsonify(message="Kata sandi yang kamu masukkan salah"),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        return jsonify(message="success")
