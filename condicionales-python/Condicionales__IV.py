# operadores logicos AND, OR, IN.

# programa para calcular merecedores de becas: 
# DISTANCIA > 40 km
# hermanos > 2
# salario > 20000


print("programa de becas 2019:")
dis_escuela=int(input("introduce la distancia en km: "))
num_hermanos=int(input("introduce numero de hermanos: "))
sal_familiar=int(input("introduce el salario familiar mensual: "))

if  dis_escuela>40 and num_hermanos>2 and sal_familiar<=20000:
	print("Si tiene derecho a beca. ")
else:
	print("No tienes derecho a beca. ")
