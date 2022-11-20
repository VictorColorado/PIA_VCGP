import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.tables()

rows = cursor.fetchall()

for row in rows:
    print (row.table_name)
    
cursor.close()
cnxn.close()
print('La conexion a sido existosa')