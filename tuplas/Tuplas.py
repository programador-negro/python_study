# Las Tuplas:

#Que son: la tuplas son listas inmjutables es decir que no se puedn modificar despues de su creacion.
#   - no se permite añadir, eliminar, mover, etc.
#   - permiten busquedas, es decir tienen index, posicion o como se le llame.
#   - si permiten comprobar si un elemento se encuentra dentro la lista. 

#Utilidad: mas rapida, menos espacio en memoria, formatean strings, pueden utilizarse como claves en un diccionario.

#Sintaxis: nombreLista=(item0,item1,item2)

#Ejecucion: 
#ejemplo 1: creando una tupla:
mitupla=("jack",1998,"kenji")
print(mitupla[2])
print("----")
#ejemplo 2: combirtiendo una tupla en una lista:
milista=list(mitupla)#lo que se esta haciendo es convertir la variable (milista) en una lista con los datos de la tupla.
print(milista)
print("----")#tambien se puede convertir una lista en una tupla usando la palabra - tuple

#ejemplo 3: saber si un elemto existe dentro de la tupla:
print("jack" in mitupla)
print("----")

#ejemplo 4: saber cuantas veces esta o existe un elemto dento la tupla
print(mitupla.count(1998))
print("----")

#ejemplo 5: saber cuantos elementos hay dentro de una tupla:
print(len(mitupla))
print("----")
#ejemplo 6: desempaquetado de tuplas:
mituplados=("juan",13,07,1784)
nombre, dia, mes, agno = mituplados 
print(nombre) # esto imprimira juan
print(dia) # esto imprimira 13
print(mes) # esto imprimira 07
print(agno) # esto imprimira 1784
print("----")