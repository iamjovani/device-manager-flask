import xlrd
import pandas as pd
from core import MySQLdb
from core import mysql



ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

#COLUMNS = ['name', 'serial number', 'operating system', 'tablet type', 'model', 'zone', 'condition', 'date', 'date damaged']



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def importfile(path):
    
   x1 = pd.ExcelFile(path) #for sheet name 
   locations = x1.sheet_names
   
   
   df = pd.read_excel (path)
   numOfRow = df.shape[0]
   
   location = locations[0]
   #usr      = 'N/A'
   
   for i in range(numOfRow):
       name         = df.at[i, 'name']
       serial_number= df.at[i, 'serial number']
       operatingsys = df.at[i, 'operating system']
       devicetype   = df.at[i, 'tablet type']
       inputmodel   = df.at[i, 'model']
       inputzone    = df.at[i, 'zone']
       state        = df.at[i, 'condition']
       dateadded    = (df.at[i, 'date'])
       datedamaged  = (df.at[i, 'date damaged'])
       #user         = df.at[i, 'user']
       
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       
       st = 'INSERT INTO `devices` (`name`, `serial_number`, `location`, `operating_sys`, `tablet_type`, `model`, `zone`, `state`, `date_added`, `date_damaged`, `user`)' \
                    'VALUES(\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")'.format(
               name, serial_number, location, operatingsys, devicetype, inputmodel, inputzone, state, dateadded, datedamaged, "NULL") # insert statment for imported items goes here
       
       cur = mysql.connection.cursor()
       cur.execute(st)
       mysql.connection.commit()
   
       print(st)
       #print( x1.sheet_names )