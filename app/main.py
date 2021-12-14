import os
# from shutil import move
from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, session
from flask_login import login_required, current_user
# from werkzeug.utils import secure_filename
# from . import db

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():

    is_admin = False

    if current_user.is_authenticated:
        permissions = current_user.permissions
        if permissions == 'admin':
            is_admin = True

    return render_template('index.html', is_admin=is_admin)

@main.route('/stream')
@login_required
def stream():

    is_admin = False

    if current_user.is_authenticated:
        permissions = current_user.permissions
        if permissions == 'admin':
            is_admin = True

    return render_template('stream.html', is_admin=is_admin)