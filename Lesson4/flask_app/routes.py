from flask import Blueprint, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from extensions import db
from models import User
from forms import RegistrationForm, LoginForm
from auth import login_required, authenticate
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username
        password = form.password
        print(username)
        print(password.data)
        hashed_password = generate_password_hash(password.data)
        print(hashed_password)
        user = User(username=username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration succesful! Log in now!', 'success')
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)
        if user:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('app.dashboard'))
        flash('Ivalid credentials!', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out', 'info')
    return redirect(url_for('app.home'))

@app.route('/')
def dashboard():
    user_count = User.query.count()
    return render_template('dashboard.html', user_count=user_count)

if __name__ == '__main__':
    app.run(debug=True)



