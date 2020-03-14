from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import timedelta
from flask import session, app
from flask.helpers import flash
from flask_mail import Mail, Message
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
#import bcrypt --- for encrypting password 

#import pandas as pd

app = Flask(__name__, template_folder="templates")

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'deviceManager'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'mullingsatberts@gmail.com',
    MAIL_PASSWORD = '!@autoparts12',
))


# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Intialize MySQL
mysql = MySQL(app)
mail = Mail(app)
db = SQLAlchemy(app)
    
#send tablet name, location and damage type in email
