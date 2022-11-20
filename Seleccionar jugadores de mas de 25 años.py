rt pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute('select Nombre from PIA where Edad >25')

for fila in cursor.fetchall():
    print(fila)
    
cursor.close()
cnxn.close()

print ("Estos son los que tiene mas de 25 años en el equipo")