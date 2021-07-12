from wtforms.validators import InputRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField, Form, ValidationError
from helpers.jwt_helper import *
from models import User
import wtforms_json

wtforms_json.init()

class ChangePasswordInput(Form):
    old_password = StringField("old_password", [
        InputRequired(message = "Password lama wajib diisi"), 
        Length(min = 8, message = "Password minimal 8 karakter")
    ])
    password = StringField("password", [
        InputRequired(message = "Password wajib diisi"), 
        Length(min = 8, message = "Password minimal 8 karakter"),
        EqualTo('confirm_password', message='Password dan konfirmasi password harus sama')
    ])
    confirm_password = StringField("confirm_password", [
        InputRequired(message = "Konfirmasi password wajib diisi"), 
        Length(min = 8, message = "Konfirmasi password minimal 8 karakter"),
        EqualTo('password', message='Password dan konfirmasi password harus sama')
    ])

class ChangeNameInput(Form):
    name = StringField("name", [InputRequired(message = "Nama wajib diisi")])

class ChangeEmaiInput(Form):
    @jwt_required()
    def unique_email(form, field):
        user = User.query.filter(User.email == field.data).filter(User.id != get_jwt_identity()).first()
        if user: 
            raise ValidationError('Alamat email sudah digunakan')

    email = StringField("email", [
        InputRequired(message = "Email wajib diisi"), 
        Email(message = "Input harus berupa alamat email"),
        unique_email
    ])
