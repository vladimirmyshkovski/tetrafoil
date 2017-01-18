# coding: utf-8
from flask import session, abort, flash, redirect, url_for
from permission import Rule
from ..models import User
from ..models import Role


class VisitorRule(Rule):
    def check(self):
        return 'user_id' not in session

    def deny(self):
        return redirect(url_for('site.index'))


class UserRule(Rule):
    def check(self):
        return 'user_id' in session

    def deny(self):
        flash('Sign in first.')
        return redirect(url_for('account.signin'))


class ManagerRule(Rule):
    def base(self):
        return UserRule()

    def check(self):
        user_id = int(session['user_id'])
        user = User.query.filter(User.id == user_id, ).first()
        if user.role == 1:
            user.role = True
        else: 
            user.role = False
        return user and user.role

    def deny(self):
        abort(403)


class AdminRule(Rule):
    def base(self):
        return UserRule()

    def check(self):
        user_id = int(session['user_id'])
        user = User.query.filter(User.id == user_id, ).first()
        if user.role == 2:
            user.role = True
        else: 
            user.role = False
        return user and user.role

    def deny(self):
        abort(403)

class SuperAdminRule(Rule):
    def base(self):
        return UserRule()

    def check(self):
        if user.role == 3:
            user.role = True
        else: 
            user.role = False
        user_id = int(session['user_id'])
        user = User.query.filter(User.id == user_id, ).first()
        return user and user.role

    def deny(self):
        abort(403)