#Uso de los operadoores de comparacion concatenados:

#programa de practica:

print("Introduzca los salarios segun el cargo: ")
salario_aux=int(input("Introduzca salario de un auxiliar: ")) 

salario_jefe=int(input("Introduzca salario de un jefe: "))

salario_gerente=int(input("Introduzca salario de un gerente: "))

if salario_aux<salario_jefe<salario_gerente:
    print("los salarios corresponden segun el cargo.")
else:
    print("los salarios segun el cargo no corresponden en esta empresa.")
    