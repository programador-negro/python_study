'''
map()
    aplica una funcion a cada elemento de una lista iterabe (listas,tuplas,etc.)
    devolviendo una lista con los resultados.
'''
class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return '{} trabaja como {} y gana un sueldo de {}'.format(self.nombre.title(),self.cargo.title(),self.salario)

lista = [
    empleado('jack','director',1234511),
    empleado('jose','administrador',123459),
    empleado('maria','abogada',123457),
    empleado('pedro','chef',123454),
    empleado('david','conductor',123456),
]
# funcion para aplciar a cada objeto
def aumento_salario(empleado):
    empleado.salario = empleado.salario*1.20
    return empleado
# Uso de la funcion map() que devolvera una lista
aumentos = map(aumento_salario, lista)
# iteracion de la lista map()
for x in aumentos:
    print(x)
