# bucles V

# veremos la funciones CONTINUE y ELSE

for i in range(10):
	if(i==1):
		continue
		#Cuando el bucle llegue a la vuelta 5 omitira este numero y saltara al siguiente
	print(i)

print("- - - -")
print("Programa para validar si un nombre usa la letra L.")
nom=input("ingrese una palabra: ")
for i in nom:
	if(i=="l"):
		nombre=True
		print(nombre)
else: # este else se usa en el bucle for, tambien cumple la misma funcion que en el condicional if.
	nombre=False
	print(nombre)