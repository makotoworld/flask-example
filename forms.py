#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import *
from wtforms.validators import *


sample = [
(u'', u''),
(u'', u''),
]
# http://wtforms.simplecodes.com/docs/

class ExampleForm(Form):
    title = TextField(u'タイトル', validators=[
            Required(u"↓&nbsp;タイトルを入力してください"),
        ])
    author = TextField(u'作者名', validators=[
            Required(u"↓&nbsp;作者名を入力してください"),
        ])
    create_date = RadioField(u'作成日', validators=[
            Required(u"↓&nbsp;作成日を入力してください"),
        ])
    description = SelectField(u'概要', validators=[
            Required(u"↓&nbsp;概要を入力してください"),
        ])
    file_name = TextField(u'ファイル名', validators=[
            Required(u"↓&nbsp;ファイル名入力してください"),
        ])
    link = TextField(u'作品リンク', validators=[
            Required(u"↓&nbsp;リンクを入力してください"),
        ])
