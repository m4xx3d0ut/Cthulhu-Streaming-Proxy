import pyotp
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/admin')
def admin():
    return render_template('admin.html')

@auth.route('/admin', methods=['POST'])
def admin_post():
    email = request.form.get('email')
    name = request.form.get('name')
    
    password = request.form.get('password')
    secret = pyotp.random_base32()
    permissions = request.form.get('permissions')

    # Check if user/email already exits in database
    user = User.query.filter_by(email=email).first() 

    # If user exists, redirect back to admin page
    if user:
        flash('Email address already in use!')
        return redirect(url_for('auth.admin_post'))

    # Create user and hash password
    new_user = User(email=email, name=name, \
    password=generate_password_hash(password, method='sha256'), \
    secret=secret, permissions=permissions)

    # Add user to database
    db.session.add(new_user)
    db.session.commit()

    flash('New user created!')
    flash('Email: %s' % email)
    flash('Password: %s' % password)
    flash('Secret: %s' % secret)

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return render_template('logout.html')