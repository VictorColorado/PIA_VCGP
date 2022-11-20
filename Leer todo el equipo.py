import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute('select * from PIA')

for fila in cursor.fetchall():
    print(fila)
    
cursor.close()
cnxn.close()

print ("Aqui se ve el mejor equipo")