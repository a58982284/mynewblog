# coding=utf-8
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


@main.route('/edit-profile', methods=['GET', ['POST']])
@login_required
def edit_profile():
    form = EditProfileAdminForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('你的个人资料已经成功更新.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data =current_user.about_me
    return render_template('edit_profile.html', form=form)
