# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])

    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('保持我的登陆状态')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):
