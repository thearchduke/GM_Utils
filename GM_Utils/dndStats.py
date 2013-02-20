from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

import os

import sqlite3


def getMonster(name):
    conn = sqlite3.connect('/home/tynan/Documents/PiPToKi/GM_Utils/dnd35.db')
    cur = conn.cursor()

    payload = [name.title()]

    cur.execute('SELECT * FROM monster WHERE name = ?', payload)

    cols = [x[0] for x in cur.description]
    rows = []

    for row in cur.fetchall():
        rows.append(row)
	
    dndObj = dict(zip(cols, rows))

    conn.close()
	
    return dndObj
