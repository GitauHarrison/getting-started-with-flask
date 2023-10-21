from app import app, db
from app.models import User
from flask_login import login_user, logout_user, \
    login_required, current_user
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, ResetPasswordRequestForm,\
    ResetPasswordForm
from datetime import datetime
from app.email import send_password_reset_email


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Reset password URL"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template(
        'reset_password.html',
        title='Reset Password',
        form=form)


@app.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset():
    """Request password reset URL"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template(
        'request_password_reset.html',
        title='Request Password Reset',
        form=form)


@app.route('/',  methods=['GET', 'POST'])
@app.route('/home',  methods=['GET', 'POST'])
@login_required
def index():
    """Index URL"""
    return render_template('index.html', title='Home')


@app.route('/<username>/profile')
@login_required
def profile(username):
    """About Me URL"""
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', title='Profile', user=user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.username.data} has been registered successfully.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
