import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute('select * from PIA where sueldo >1250000')

for fila in cursor.fetchall():
    print(fila)
    
cursor.close()
cnxn.close()

print ("Estos son los que ganan mas de 1250000")
