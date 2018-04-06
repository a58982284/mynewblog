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
    email = StringField('Email', validators=[DataRequired(). Length(1,64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1,64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               '用户名必须只包含字母,数字,点或下划线')])

    password = PasswordField('密码', validators=[
        DataRequired(),EqualTo('password2', message='密码必须保持一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('Register')
