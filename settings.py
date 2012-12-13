#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import *
import platform

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

if platform.system() == "Windows":
    #UPLOAD_FOLDER
    UPLOAD_FOLDER = 'D:/code/example/static/img'

    # configure our database
    DATABASE = {
    # sqlite3
    #    'name': '/home/SepAnalytices/htdocs/app/sep.db',
    #    'name': 'D:/code/SepAnalytices/sep.db',
    #    'engine': 'peewee.SqliteDatabase',
    # mysql
        'name': 'sep',
        'user': 'root',
        'host': 'localhost',
        'passwd': 'mk12fss',
        'engine': 'peewee.MySQLDatabase',
    }
elif platform.system() == "Darwin":
    #UPLOAD_FOLDER
    UPLOAD_FOLDER = '/home/example/htdocs/app/static/img'

    # configure our database
    DATABASE = {
    # sqlite3
    #    'name': '/home/example/htdocs/app/sep.db',
    #    'engine': 'peewee.SqliteDatabase',
    # mysql
        'name': 'sep',
        'user': 'root',
        'host': 'localhost',
        'passwd': 'mk12fss',
        'engine': 'peewee.MySQLDatabase',
    }
elif platform.system() == "Linux":
    #UPLOAD_FOLDER
    UPLOAD_FOLDER = '/home/example/htdocs/app/static/img'

    # configure our database
    DATABASE = {
    # sqlite3
    #    'name': '/home/example/htdocs/app/sep.db',
    #    'engine': 'peewee.SqliteDatabase',
    # mysql
        'name': 'sep',
        'user': 'root',
        'host': 'localhost',
        'passwd': 'mk12fss',
        'engine': 'peewee.MySQLDatabase',
    }

#SECRET_KEY
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)
