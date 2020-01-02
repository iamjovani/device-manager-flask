import sqlController

columns = {
  
    "accounts": ("(", "id", "username", "password", "email", ")"), 
    "devices": ("(", "name", "serial_number", "installed_by", "operating_sys", "tablet_type", "model", "zone", "condition", "date_added", "date_damaged", ")")
}




def test():
    name = "John Brown"
    serialnum = "1283986743"
    installby = "Paul Rowe"
    operatingsys = "Windows 10"
    devicetype = "PRO 3"
    inputmodel = "N/A"
    inputzone = "ZONE 1"
    condition= "GOOD"
    dateadded = "2015-12-17"
    datedamaged = "2015-12-17"
    
    
    
    conn = sqlController.databaseGenerator("deviceManager", columns)
    conn.addRecord(["'"+ name+"'", "'"+serialnum+"'", "'"+installby+"'","'"+operatingsys+"'", 
                             "'"+devicetype+"'", "'"+inputmodel+"'", "'"+inputzone+"'", "'"+condition+"'", "'"+dateadded+"'", "'"+datedamaged+"'"], "devices")
    
test()