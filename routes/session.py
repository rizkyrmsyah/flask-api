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
        if request.form:
            input_request = request.form
            inputs = RegisterInput(request.form)
        else:
            input_request = request.get_json()
            inputs = RegisterInput.from_json(input_request)
        
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.register(input_request)

    @blueprint.route("login", methods = ["POST"])
    def login():
        if request.form:
            input_request = request.form
            inputs = LoginInput(request.form)
        else:
            input_request = request.get_json()
            inputs = LoginInput.from_json(input_request)

        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.login(input_request)
    
    @blueprint.route("check-password", methods = ["POST"])
    def check_password():
        if request.form:
            input_request = request.form
            inputs = CheckPaswordInput(request.form)
        else:
            input_request = request.get_json()
            inputs = CheckPaswordInput.from_json(input_request)

        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return sessionController.check_password(input_request)