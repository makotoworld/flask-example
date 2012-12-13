#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask_peewee.db import Database
from peewee import *

from settings import *

# instantiate the db wrapper
db = Database(app)

# Field types table
# http://peewee.readthedocs.org/en/latest/peewee/models.html#fields
# Field Type    Sqlite    Postgresql    MySQL
# CharField    varchar    varchar    varchar
# TextField    text    text    longtext
# DateTimeField    datetime    timestamp    datetime
# IntegerField    integer    integer    integer
# BooleanField    smallint    boolean    bool
# FloatField    real    real    real
# DoubleField    real    double precision    double precision
# BigIntegerField    integer    bigint    bigint
# DecimalField    decimal    numeric    numeric
# PrimaryKeyField    integer    serial    integer
# ForeignKeyField    integer    integer    integer
# DateField    date    date    date
# TimeField    time    time    time

# models
class Contents(db.Model):
    content_id = IntegerField()
    title = CharField()
    content = CharField()
    updated = CharField(default='0000-00-00 00:00:00')
    created = DateTimeField(default=datetime.datetime.now)

