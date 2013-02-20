from flask import Flask, render_template, request, session
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required

from GM_Utils import views, app, mail, models, db

if __name__ == '__main__':
    app.run()
