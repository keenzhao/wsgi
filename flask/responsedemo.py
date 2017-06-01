#!/usr/bin/python
# coding=utf-8


from flask import make_response,app


@app.route('/login')
def login():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('age', 42)
    return response
