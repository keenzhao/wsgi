#!/usr/bin/python
# coding=utf-8

from flask import Flask
# from flask import abort
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 表单类 一个简单的Web 表单，包含一个文本字段和一个提交按钮
class NameForm(FlaskForm):
    name = StringField('输入测试数据?', validators=[DataRequired()])
    submit = SubmitField('提交')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<h3>you browser is %s</h3>' % user_agent
    return render_template('index.html', user_agent=user_agent)


@app.route('/forms', methods=['GET', 'POST'])
def forms_demo():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
    form.name.data = ''
    return render_template('formsdemo.html', form=form, name=name)


@app.route('/redirect', methods=['POST', 'GET'])
def redirect_forms():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('看上去你已经改变了你的名字！名字数据从【'+old_name+"】改变到【"+form.name.data+"】")
        session['name'] = form.name.data
        return redirect(url_for('redirect_forms'))

    return render_template('formsdemo.html', form=form, name=session.get('name'))


@app.route('/super')
def super():
    return render_template('extendsdemo.html')


@app.route('/test/<name>')
def test(name):
    comments = ['python', 'java', 'C#', 'C++', 'Php', 'R', 'Ruby']
    return render_template('bootstrapdemo.html',
                           name=name,
                           comments=comments,
                           current_time=datetime.utcnow())


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


@app.route('/redirect163')
def to():
    return redirect('http://www.163.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


if __name__ == '__main__':
    # manager.run()
    app.run(debug=True, port=8080)
