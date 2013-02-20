from flask import Flask, render_template, request, session
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required

from GM_Utils import app, db

import dndStats

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secrets')
@login_required
def secrets():
    return "Authorization successful"
    

@app.route('/monsters/<name>')
def monsters(name):
    monster=dndStats.getMonster(name)
    return str(monster)
