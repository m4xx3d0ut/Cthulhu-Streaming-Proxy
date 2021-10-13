import os
# from shutil import move
from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, session
# from flask_login import login_required, current_user
# from werkzeug.utils import secure_filename
# from . import db

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')