import mysql.connector

#attributes needed for the specification of columns in a table 
columns = {
  
    "account": ("(", "id", "username", "password", "email", ")"), 
    "devices": ("(", "name", "serial_number", "installed_by", "operating_sys", "tablet_type", "model", "zone", "condition", "date_added", "date_damaged", ")")
    
}


class databaseGenerator:
    def __init__(self, dbname, columns):
        self.dbname   = dbname
        self.column   = columns
        self.mydb     = mysql.connector.connect(host="localhost", user="root", passwd="", database=dbname)
        self.mycursor = self.mydb.cursor()

    # attrib is a list of the arributes for the record, 
    # table is the string with the name of the table 
    #NB: if the datatype in the db is varchar the arrib
    #value in the list should be represented as a quoted string
    def addRecord(self, attrib, name):
        try:
            strstatement  =""
            strstatement  ="INSERT INTO "+str(name)+" "+ "".join(self.column[name])
            strstatement += ' VALUES({});'.format(','.join("{0}".format(x) for x in attrib))
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for addRecord")

    #key is the identifier of the value to be removed
    #name is the name of the table to removed the record form
    #coltocompare is the name of the column to compare primkey against
    #NB: primkey must be a quoted string if datatype is varchar 
    def removeRecord(self, key, name, coltocompare):
        try:
            strstatement  = ""
            strstatement  = "DELETE FROM "+str(name)
            strstatement += " WHERE {} = {};".format(coltocompare, key)
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for removeRecord")

    #name of table must be python string
    def showTableAll(self, tableName):
        try:
            strstatement = ""
            strstatement = "SELECT * FROM {};".format(tableName)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input for showTableAll")

    #key must be quoted string if the datatype in the database is varchar or date
    #tableName - the name of the table to be updated
    # columntoupdate - name of column to be updated
    # selection - is the column to be selected
    #key - the unique identifier of the record
    #NT
    def showTableCondition(self, tableName, coltocompare, key, selection):
        try:
            strstatement = ""
            strstatement = "SELECT {} FROM {} WHERE {} = {};".format(selection, tableName, coltocompare, key)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input for showTableCondition")
        
    #key must be quoted string if the datatype in the database is varchar or date
    #tableName - the name of the table to be updated
    # columntoupdate - name of column to be updated
    # value - is the new value of the column
    #key - the unique identifier of the record
    #idfn - the column to compare to key in order to find specified record
    def updateRecord(self, tableName, columntoupdate, key, value, idfn ):
        try:
            strstatement = ""
            strstatement = "UPDATE {} SET {} = {} WHERE {} = {};".format(tableName, columntoupdate, value, idfn, key )
            self.mycursor.execute(strstatement)
        except:
            print("Pease check input for updateRecord")


    #tableName - the name of the table to be updated
    # column - name of column to be updated
    # value - is the new value of the column 
    def updateTable(self, tableName, column, value):
        try:
            strstatement = ""
            strstatement = "UPDATE {} SET {} = {};".format(tableName, column, value)
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for updateTable")


    def orderByPrice(self, ordr):
        try:
            strstatement = "CALL orderByPrice(\"{}\");".format(ordr)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input data type for orderByPrice")

    
    def getByName(self, name):
        try:
            strstatement = "CALL getByName(\"{}\");".format(name)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input data type for getByName")


    def getByModel(self, model):
        try:
            strstatement = "CALL getByModel(\"{}\");".format(model)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input data type for getByModel")


    def getByBrand(self, brand):
        try:
            strstatement = "CALL getByBrand(\"{}\");".format(brand)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input data type for getByBrand")
            

    def getBranchByCount(self, column, colkey, condition):
        try:
            strstatement = "SELECT COUNT(*) FROM {} WHERE {} LIKE '%{}%';".format(column, colkey, condition)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except mysql.connector.Error as error:
            print("Please check getBranchByCount {}".format(error))

    def getBranchCount(self, column, colkey):
        try:
            strstatement = "SELECT COUNT(*) FROM {};".format(column, colkey)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except mysql.connector.Error as error:
            print("Please check getBranchByCount {}".format(error))
    #destructor closes database and connection
    def __del__(self): 
        self.mycursor.close()
        self.mydb.close()


if __name__ == "__main__":
    db = None
    db = databaseGenerator("compustore", columns)
    
    #testing code
    #tb = db.showTableCondition("test", "Username", "\"popii\"", "Password")
    #print(tb)
    #t  = db.showTableAll("test")
    #print(t)
    #db.updateRecord("managers", "person_name", "\"john\"","\"Grim\"", "person_name") 
    #db.updateTable("test", "id", "1234*2")

    #db.addRecord(["\"1234\"", "\"hviujk\"", "\"gdfku\"","\"hjfgf\""], "test")
    #db.addRecord(["\"john\"", "\"samuels\""], "managers")
    #n.addRecord([7564, 657437,], "creditcard")
    #db.removeRecord("\"Luke\"", "managers", "manager_name")