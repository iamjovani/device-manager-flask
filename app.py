from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import timedelta
from flask import session, app
from flask.helpers import flash

import pandas as pd

app = Flask(__name__, template_folder="templates")

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'deviceManager'

# Intialize MySQL
mysql = MySQL(app)


@app.before_request
def make_session_permanent(): #Session expires after 5 mins
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

# http://localhost:5000/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)


# http://localhost:5000/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


# http://localhost:5000/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
           # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account, username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        #Load table
        cursor.execute('SELECT * FROM devices')
        data = cursor.fetchall()
        # Show the profile page with 
        return render_template('dashboard.html', username=session['username'], values=data) # values not transmitting to table
    return redirect(url_for('login'))


@app.route('/add',  methods=['POST'])
def add():
  if 'loggedin' in session:
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
       account = cursor.fetchone()

       try:
           if request.method == 'POST':
               name = request.form.get('inputDeviceName')
               serialnum = request.form.get('inputSerialNumber')
               location = request.form.get('inputLocation')
               operatingsys = request.form.get('inputOperatingSys')
               devicetype = request.form.get('inputDeviceType')
               inputmodel = request.form.get('inputModel')
               inputzone = request.form.get('inputZone')
               condition = request.form.get('inputCondition')
               dateadded = request.form.get('inputDateAdded')
               datedamaged = request.form.get('inputDateDamaged')

               st = 'INSERT INTO `devices` (`name`, `serial_number`, `location`, `operating_sys`, `tablet_type`, `model`, `zone`, `condition`, `date_added`, `date_damaged`)' \
                    'VALUES(\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")'.format(
                        name, serialnum, location, operatingsys, devicetype, inputmodel, inputzone, condition, dateadded, datedamaged)
               cur = mysql.connection.cursor()
               cur.execute(st)
               mysql.connection.commit()
           return redirect(url_for("dashboard", username=session['username']))
       
       except ValueError as error:
           flash("Failed to insert record into table {}".format(error))
           
           
@app.route('/dashboard/<string:id_data>', methods = ['GET'])        
def delete(id_data):
    try:
        if 'loggedin' in session:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
            account = cursor.fetchone()
           
            cursor.execute("DELETE FROM devices WHERE serial_number=%s", (id_data,))
            mysql.connection.commit()
            flash("Record Has Been Deleted Successfully")
        return redirect(url_for("dashboard", username=session['username']))
       
    except ValueError as error:
        flash("Failed to insert record into table {}".format(error))   

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

if __name__ == '__main__':
   app.run(debug = True)