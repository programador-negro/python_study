# Diccionarios:

#Que son: Estrutura de datos que nos permite alamcenas valores de diferente tipo e incluso listas y otros diccionarios.
# - una de las caracteristicas es que los datoos se almacenan asociadosa una clave de tal forma que se crea una asociacion de tipo CLAVE:VALOR para cada elemento almacenado.
# - los elementos almacenados no estan ordenados como en una lista o tupla.

#Utilidad: nombreDiccionario={"clave":"valor","clave":"valor"}

#Sintaxis: nombreDiccionario={"clave":"valor","clave":"valor"}

#Ejecucion:
#ejemplo 1: creando un diccionario:
midic={"colombia":"bogota","estadosunidos":"washintong","españa":"madrid"}
print(midic["colombia"])
print("----")


#ejemplo 2: cambiar o agregar un valor a una clave:
midic["colombia"]="medellin"
print(midic)

#ejemplo 3: eliminar el valor de una clave:
del midic["estadosunidos"]
print(midic)
print("----")

#ejemplo 4: almacennar valores de una tupla dentro de un dicci
tupla = ("nombre","apellido","edad")
midicdos={tupla[0]:"jack",tupla[1]:"ybarra",tupla[2]:20}
print(midicdos)#imprimir todo el diccionario
print(midicdos["nombre"])#imprimir cierto valor del diccionario con dato de la tupla
print("----")

#ejemplo 5: alamacenar una tupla dentro de un diccionario.
midictres={"color":"rojo","tamaño":34.5,"numeros":[4,5,6,7,8]}
print(midictres["numeros"])
print("----")

#ejemplo 6: almacenar un diccionario dentro de otro diccionario:
midicuatro={"color":"rojo","tamaño":34.5,"datos":{"nombre":"jack","apellido":"ybarra"}}
print(midicuatro["datos"])
print("----")

#ejemplo 7: imprimir solo las claves (keys)
print(midicuatro.keys())
print("----")

#ejemplo 8: imprimir solo los valores (values)
print(midicuatro.values())
print("----")

#ejemplo 9: contar cuantos elemtos tiene el diccionario:
print(len(midicuatro))
print("----")