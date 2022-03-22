# SUBCONSULTAS
	# IN significa si existe dentro  de.
SELECT * FROM usuarios WHERE id IN (SELECT usuario_id FROM entradas);