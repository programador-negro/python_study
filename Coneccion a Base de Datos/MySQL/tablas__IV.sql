# Consulta para mostrar todos los registros de una tabla
SELECT email, nombre, apellidos FROM usuarios;

# Consulta con condicion:
SELECT * FROM usuarios WHERE  email = 'jack@mail.com';

# Mostrar todos los registros
SELECT * FROM usuarios;
#- - - - - - - - - - - -
# Operadores aritmeticos dentro las consultas
SELECT email, (4+4) as 'operacion' FROM usuarios;
# (4+4) as 'operacion' hace que se imprima una columna extra
# con el titulo 'operacion' y el resultado de 4+4

SELECT email, (id+4) as 'operacion' FROM usuarios;
# tambien se pueden usar llos campos ppara hacer operaciones.
#- - - - - - - - - - - - 

# Funciones aritmeticas
