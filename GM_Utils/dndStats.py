from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

import os

import sqlite3

conn = sqlite3.connect('dnd35.db')
cur = conn.cursor()

payload = ['Troll']

cur.execute('SELECT * FROM monster WHERE name = ?', payload)

cols = [x[0] for x in cur.description]
rows = []

for row in cur.fetchone():
	rows.append(row)

dndObj = dict(zip(cols, rows))


print dndObj
