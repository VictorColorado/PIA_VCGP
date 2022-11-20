import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute('select AVG(Sueldo) from PIA ')

for fila in cursor.fetchall():
    print(fila)
    
cursor.close()
cnxn.close()

print ("Este es el promedio de todos los sueldos")