# coding: utf-8
from itsdangerous import URLSafeSerializer, BadSignature
from flask import current_app
from flask_security import Security, SQLAlchemyUserDatastore
from application.models import User, Role, db

security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role) 


def encode(something):
    """Encode something with SECRET_KEY."""
    secret_key = current_app.config.get('SECRET_KEY')
    s = URLSafeSerializer(secret_key)
    return s.dumps(something)


def decode(something):
    """Decode something with SECRET_KEY."""
    secret_key = current_app.config.get('SECRET_KEY')
    s = URLSafeSerializer(secret_key)
    try:
        return s.loads(something)
    except BadSignature:
        return None
