#!/usr/bin/python
# coding=utf-8

from flask import Flask
# from flask import abort
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<h3>you browser is %s</h3>' % user_agent
    return render_template('index.html', user_agent=user_agent)


@app.route('/super')
def super():
    return render_template('extendsdemo.html')


@app.route('/test/<name>')
def test(name):
    comments = ['python', 'java', 'C#', 'C++', 'Php', 'R', 'Ruby']
    return render_template('bootstrapdemo.html',
                           name=name,
                           comments=comments)


@app.route('/user/<string:name>')
def user(name):
    list1 = range(10)
    list2 = ['python', 'java', 'C#', 'C++', 'Php', 'R', 'Ruby']
    return render_template('jinja2demo.html',
                           user=name,
                           listtest=list1,
                           list2=list2)
    # if name != 'keen':
    #     abort(404)
    # return 'welcome %s,   cookie:age=%s' % (name, request.cookies.get('age'))


@app.route('/login')
def login():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('age', '42')
    return response


@app.route('/redirect')
def to():
    return redirect('http://www.163.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


if __name__ == '__main__':
    # manager.run()
    app.run(debug=True, port=8080)
