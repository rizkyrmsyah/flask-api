from flask import Blueprint, request, jsonify
from config import configuration
from validations.user_input import *
from http import HTTPStatus
from controllers import UserController
import json

blueprint = Blueprint("user", __name__)
userController = UserController()

class User:
    
    @blueprint.route("/", methods = ["GET"])
    def show():
        return userController.show()

    @blueprint.route("change-password", methods = ["POST"])
    def change_password():
        if request.form:
            input_request = request.form
            inputs = ChangePasswordInput(request.form)
        else:
            input_request = request.get_json()
            inputs = ChangePasswordInput.from_json(input_request)

        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return userController.change_password(input_request)
    
    @blueprint.route("change-name", methods = ["POST"])
    def change_name():
        if request.form:
            input_request = request.form
            inputs = ChangeNameInput(request.form)
        else:
            input_request = request.get_json()
            inputs = ChangeNameInput.from_json(input_request)

        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY
            
        return userController.change_name(input_request)