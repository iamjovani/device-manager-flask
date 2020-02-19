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
   df = pd.read_excel (path)
   numOfRow = df.shape[0]
   
   for i in range(numOfRow):
       name = df.at[i, 'name']
       serial_number = df.at[i, 'serial number']
       operating_sys = df.at[i, 'operating system']
       tablet_type   = df.at[i, 'tablet type']
       model         = df.at[i, 'model']
       zone          = df.at[i, 'zone']
       condtion      = df.at[i, 'condition']
       date          = df.at[i, 'date']
       date_damaged  = df.at[i, 'date damaged']
       
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       
       st = '' # insert statment for imported items goes here
       
       cur = mysql.connection.cursor()
       cur.execute(st)
       mysql.connection.commit()
   
       print(name)