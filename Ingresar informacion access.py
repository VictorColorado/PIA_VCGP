import pyodbc

cnxn = pyodbc.connect("DSN=PIA")

cursor = cnxn.cursor()

cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Victor C.','Turno_1','Zurdo','Center_field',31,2000000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Jorge Q.','Turno_7','Derecho','Shortstop',26,2500000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Carlos J.','Turno_8','Zurdo','Catcher',36,1240000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Luis C.','Turno_6','Derecho','Firt_Base',20,800000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Armando R.','Turno_4','Derecho','Second_Base',23,1670000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Diego R.','Turno_3','Zurdo','Third_Base',28,1100000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Jose R.','Turno_5','Derecho','Rigth_field',34,1500000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Raul S.','Turno_2','Derecho','left_field',25,1250000)")
cursor.execute("insert into PIA(Nombre, Turno, Mano_dominante, Posicion, Edad, Sueldo) values('Roberto M.','Sin_turno','Derecho','Bd',23,120000)")

cnxn.commit()

cursor.close()
cnxn.close()

print ("Se a ingresado la informacion")