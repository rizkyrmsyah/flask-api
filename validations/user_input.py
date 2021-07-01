from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField

class ChangePasswordInput(FlaskForm):
    old_password = StringField("old_password", [InputRequired(message = "Password lama wajib diisi"), Length(min = 8, message = "Password minimal 8 karakter")])
    password = StringField("password", [InputRequired(message = "Password wajib diisi"), Length(min = 8, message = "Password minimal 8 karakter")])
    confirm_password = StringField("confirm_password", [InputRequired(message = "Konfirmasi password wajib diisi"), Length(min = 8, message = "Konfirmasi password minimal 8 karakter")])

class ChangeNameInput(FlaskForm):
    name = StringField("name", [InputRequired(message = "Nama wajib diisi")])
