from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app,request,url_for
from flask_login import UserMixin, AnonymousUserMixin
from app.exceptions import ValidationError
from . import db,login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64),unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Interger,db.Foreignkey('roles.id'))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen =db.Column(db.DateTime(), default=datetime.utcnow)


    @staticmethod

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))