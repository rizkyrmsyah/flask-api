from wtforms.validators import InputRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField, Form, ValidationError
from models import User
import wtforms_json

wtforms_json.init()

class RegisterInput(Form):
    def unique_email(form, field):
        user = User.query.filter_by(email = field.data).first()
        if user: 
            raise ValidationError('Alamat email sudah digunakan')
        
    name = StringField("name", [InputRequired(message = "Silakan masukkan nama kamu")])
    email = StringField("email", [
        InputRequired(message = "Silakan masukkan alamat email kamu"), 
        Email(message = "Alamat email tidak valid"),
        unique_email
    ])
    password = StringField("password", [
        InputRequired(message = "Silakan masukkan kata sandi kamu"), 
        Length(min = 8, message = "Kata sandi harus mengandung setidaknya 8 karakter")
    ])
    confirm_password = StringField("confirm_password", [
        InputRequired(message = "Silakan masukkan konfirmasi kata sandi kamu"), 
        Length(min = 8, message = "Konfirmasi kata sandi harus mengandung setidaknya 8 karakter"),
        EqualTo('password', message='Konfirmasi kata sandi kamu tidak sama')
    ])

class LoginInput(Form):
    email = StringField("email", [
        InputRequired(message = "Silakan masukkan alamat email kamu"), 
        Email(message = "Alamat email tidak valid")
    ])
    password = StringField("password", [InputRequired(message = "Silakan masukkan kata sandi kamu")])

class CheckPaswordInput(Form):
    password = StringField("password", [
        InputRequired(message = "Silakan masukkan kata sandi kamu"), 
        Length(min = 8, message = "Kata sandi harus mengandung setidaknya 8 karakter")
    ])
