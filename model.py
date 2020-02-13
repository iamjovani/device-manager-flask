import xlrd
import pandas as pd



ALLOWED_EXTENSIONS = {'csv', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def importfile(path):
   df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx') 