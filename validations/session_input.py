from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField
import wtforms_json

wtforms_json.init()

class RegisterInput(FlaskForm):
    name = StringField("name", [InputRequired(message = "Nama wajib diisi")])
    email = StringField("email", [InputRequired(message = "Email wajib diisi"), Email(message = "Input harus berupa alamat email")])
    password = StringField("password", [InputRequired(message = "Password wajib diisi"), Length(min = 8, message = "Password minimal 8 karakter")])
    confirm_password = StringField("confirm_password", [InputRequired(message = "Konfirmasi password wajib diisi"), Length(min = 8, message = "Konfirmasi password minimal 8 karakter")])

class LoginInput(FlaskForm):
    email = StringField("email", [InputRequired(message = "Email wajib diisi"), Email(message = "Input harus berupa alamat email")])
    password = StringField("password", [InputRequired(message = "Password wajib diisi")])

class CheckPaswordInput(FlaskForm):
    password = StringField("password", [InputRequired(message = "Password wajib diisi"), Length(min = 8, message = "Konfirmasi password minimal 8 karakter")])