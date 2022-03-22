#Caso prueba dos: confirmando la existencia de varios valores con un If - Else:
var=raw_input("ingrese un nombre por pantalla: ")
while True:
    if var in ("daniel","flor","felipe","diego"):
        print("nombre correcto")
        break
    else:
        print("nombre incorrecto") 