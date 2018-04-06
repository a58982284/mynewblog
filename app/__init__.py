# coding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from  flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown


login_manager = LoginManager()
login_manager.login_view = 'auth.login' #登录视图的名称可以设置成 LoginManager.login_view


def create_app(config_name):
    app = Flask(__name__)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    form.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')