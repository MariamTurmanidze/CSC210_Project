
import sqlite3
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db, bcrypt
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route("/")
def index(): 
	return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template('profile.html', title='Profile')


@app.route("/success")
def success():
    return render_template('success.html', title='Registration Successful')


@app.route("/register", methods = ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(employee_id=form.employee_id.data,lname=form.lname.data, fname=form.fname.data,
                    ssn=form.ssn.data, email=form.email.data, address=form.address.data,
                    dep_name=form.dep_name.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered employee!')
        return redirect(url_for('success'))
    return render_template('register.html', title='Register', form=RegistrationForm())
    

@app.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
           return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
           user = User.query.filter_by(employee_id=form.employee_id.data).first()
           if user and bcrypt.check_password_hash(user.password, form.password.data):
                   login_user(user, remember=form.remember_me.data)
                   #next_page = request.args.get('next')
                   #return redirect(next_page) if next_page else redirect(url_for('index'))
                   return render_template('profile.html', title='Profile', employee_id=form.employee_id.data)
           else:
                   flash('Failed Login. Incorrect Employee ID or Password')
        return render_template('login.html', title='Sign In', form=form)
    


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route("/secret")
@login_required
def secret():
  return "Only authenticated users are allowed!"



        
