# Ejemplo con la sentencia o condicional IF:
print("Programa para evaluar alumnos")
notaAlumno=input()
#tambien se puede escribir:
# notaAlumno("escribe aqui tu calificacion: ")

def evaluacion(nota):
    valoracion="aprobado"
    if(nota>=5):
        print(valoracion)
    else:
        print("reprobado")
        
evaluacion(notaAlumno)
# es posible que en algunas versiones de python se requiera escribir el tipo de variable que entra por teclado:
# evaluacion(int(notaAlumno)) - ya que el input solo acepta strings