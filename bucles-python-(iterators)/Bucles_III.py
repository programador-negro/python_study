# bucle for con range()
for i in range(1,10):
	print("Hola")
	print(i)
print("- - - -")

# bucle range con tres argumentos
for i in range(1,10,2): # el tercer argumento indica que imprima los numeros de dos en dos(en este caso por ser 2)
	print("Hola")
	print(i)
print("- - - -")


# concatenar texto con variable en un buble
for i in range(1,5):
	print(f"valor de la variable i es {i}") # la letra f es una funcion que permite concatenar texto y variable. de lo contrario todo se imprime como texto
print("- - - -")

# comprobar una direccion de email con un bucle for y a funcion len()
# len() cuenta la cantidad de caracteres.
validar=False
email=input("Introduce tu email: ") 
for i in range(len(email)): # cuenta lla cantidad de caracteres de 'email'
	if email[i]=="@": # en cada vuelta de bucle revisa si el caracter en la posicion i es = @ (es ccomo si convirtiera email en unarray)
		validar=True
if validar:
	print("Email correcto")
else:
	print("Email incorrecto")
