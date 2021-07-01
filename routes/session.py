from flask import Blueprint, request, jsonify
from config import configuration
from validations.session_input import *
from http import HTTPStatus
from controllers import SessionController
import json

blueprint = Blueprint("session", __name__)
sessionController = SessionController()

class Session:
    
    @blueprint.route("register", methods = ["POST"])
    def register():
        inputs = RegisterInput(request.form, meta = {'csrf': False})
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.register(request.form)

    @blueprint.route("login", methods = ["POST"])
    def login():
        inputs = LoginInput(request.form, meta = {'csrf': False})
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.login(request.form)
    
    @blueprint.route("check-password", methods = ["POST"])
    def check_password():
        inputs = CheckPaswordInput(request.form, meta = {'csrf': False})
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.check_password(request.form)