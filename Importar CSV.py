import pandas as pd

SEPARADOR = ("*"*20)+"\n"

Equipo = {\
    "Victor C.":["Turno_1","Zurdo","Center_field",31,2000000], \
    "Jorge Q.":["Turno_7","Derecho","Shortstop",26,2500000],\
    "Carlos J.":["Turno_8","Zurdo","Catcher",36,1240000],\
    "Luis C.":["Turno_6","Derecho","Firt_Base",20,800000],\
    "Armando R.":["Turno_4","Derecho","Second_Base",23,1670000],\
    "Diego R.":["Turno_3","Zurdo","Third_Base",28,1100000],\
    "Jose R.":["Turno_5","Derecho","Rigth_field",34,1500000],\
    "Raul .S":["Turno_2","Derecho","left_field",25,1250000],\
    "Roberto M.":["Sin turno","Derecho","Bd",23,120000]
    }
Jugadores = pd.DataFrame(Equipo)
Jugadores.index = ["Turno al bat", "Mano dominante", "Posicion","Edad","Sueldo"]

Jugadores.to_csv(r'Jugadores.csv', index=True, header=True)
print("El archivo CSV a sido creado")