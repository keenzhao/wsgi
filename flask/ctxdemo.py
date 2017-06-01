#!/usr/bin/python
# coding=utf-8

from flask_start import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()
print(current_app.name,app.url_map)
app_ctx.pop()
