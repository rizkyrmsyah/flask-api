from wtforms.validators import InputRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField, Form, ValidationError
from models import User
import wtforms_json

wtforms_json.init()

def unique_email(form, field):
    user = User.query.filter_by(email = field.data).first()
    if user:
        raise ValidationError('Email sudah terpakai')

class RegisterInput(Form):
    name = StringField("name", [InputRequired(message = "Nama wajib diisi")])
    email = StringField("email", [
        InputRequired(message = "Email wajib diisi"), 
        Email(message = "Input harus berupa alamat email"),
        unique_email
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

class LoginInput(Form):
    email = StringField("email", [InputRequired(message = "Email wajib diisi"), Email(message = "Input harus berupa alamat email")])
    password = StringField("password", [InputRequired(message = "Password wajib diisi")])

class CheckPaswordInput(Form):
    password = StringField("password", [InputRequired(message = "Password wajib diisi"), Length(min = 8, message = "Konfirmasi password minimal 8 karakter")])
