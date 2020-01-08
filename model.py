from app import session
from app import mysql
from app import MySQLdb
from app import request
from app import redirect
from app import url_for
from app import render_template
from app import flash

import pandas as pd


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


