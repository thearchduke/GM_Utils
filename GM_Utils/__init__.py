from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required
import os

# Create app
app = Flask(__name__)
app.config.from_object('GM_Utils.config')

# Setup mail extension
mail = Mail(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Create database connection object
db = SQLAlchemy(app)

