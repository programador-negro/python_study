# Modificar, Borrar y/o Actualizar datos.

# ejemplo 1: 
	#modificar o actualizar datos de un usuario especifico	
UPDATE usuarios SET id=2 WHERE id=3;

UPDATE usuarios SET nombre='Julian', apellidos='Miranda' WHERE id=4;

# ejemplo 2:
	# Borrar registros (!Ser cuidadoso) siempre poner un where para no borrar todo
DELETE FROM usuarios WHERE email = 'mau@mail.com';


