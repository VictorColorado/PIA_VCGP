import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute("Delete from PIA where Edad = 20")

cnxn.commit()

cursor.close()
cnxn.close()

print ("FIN)