#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import *
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication, RestResource, AdminAuthentication

from settings import *
from models import *
from forms import *

import os, sys, codecs, re
from werkzeug import secure_filename
import urllib
import urllib2
import simplejson
from datetime import *
import datetime
import locale
import random
import string
import calendar
import hashlib

# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)
#

class ContentsAdmin(ModelAdmin):
    columns = ('title', 'created')

class ContentsResource(RestResource):
    exclude = ('title', 'content', 'created')
    def get_query(self):
        return self.model.select()

admin = Admin(app, auth)
admin.register(Contents, ContentsAdmin)

admin.setup()

# instantiate the user auth
user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)

# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)

#register the Content model
api.register(Contents, ContentsResource, auth=admin_auth)
api.setup()

# customize template tag
def date_now(value):
    return datetime.datetime.now().strftime(value).decode('utf-8')

app.jinja_env.filters['date_now'] = date_now


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index(name=None):
    return render_template('index.html')


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Contents.create_table(fail_silently=True)

#    app.run(debug=True, host="0.0.0.0", port=80)
    app.run(debug=True, port=5000)

application = app
