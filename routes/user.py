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
        inputs = ChangePasswordInput(request.form, meta = {'csrf': False})
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY

        return userController.change_password(request.form)
    
    @blueprint.route("change-name", methods = ["POST"])
    def change_name():
        inputs = ChangeNameInput(request.form, meta = {'csrf': False})
        if not inputs.validate():
            return jsonify(error = inputs.errors), HTTPStatus.UNPROCESSABLE_ENTITY
            
        return userController.change_name(request.form)