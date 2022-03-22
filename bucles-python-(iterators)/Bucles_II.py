# Bucles II
# imprimir las veces segun la cantidad de caracteres:
for i in "asdfghjkl":
	print("hola", end=" ")
	# el end=" ", sirve para no hacer saltos de linea en cada repeticion
	# imprimira hola varias veecs segun la cantidad de caracteres.
print("- - - -")

# ejemplo practico
email=False
for i in "dan@gmail.com":
	if(i=="@"):
		email=True
		
if email==True:
	print("el email es correcto")
else:
	print("el email es incorrecto")
print("- - - -")

