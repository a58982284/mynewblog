from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import main
from . forms import EditProfileForm, EditProfileAdminForm, PostForm,\
    CommentForm
from .. import db
from .. models import Permission, Role, User, Post, Comment
from .. decorators import admin_required, permission_required



@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404)()

    return render_template('user.html',user=user, posts=posts, pagination=pagination)