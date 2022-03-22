# Consultas de agrupamiento
	# Mostrar el numero de entradas segun las categorias (GROUP BY).
	# debe mostrar: +-----------------+--------------+
	#				| No. de entradas | categoria_id |
	#				+-----------------+--------------+
	#				|               1 |            1 |
	#				|               1 |            2 |
	#				|               2 |            3 |
	#				|               2 |            4 |
	#				+-----------------+--------------+
SELECT COUNT(titulo) AS 'No. de entradas', categoria_id FROM entradas GROUP BY categoria_id;

	# Mostrar el numero de entradas segun las categorias teniendo en cuenta (HAVING COUNT()) una condicion
SELECT COUNT(titulo) AS 'No. de entradas', categoria_id FROM entradas GROUP BY categoria_id HAVING COUNT(titulo)>=2;
	# debe mostrar: +-----------------+--------------+
	#				| No. de entradas | categoria_id |
	#				+-----------------+--------------+
	#				|               2 |            3 |
	#				|               2 |            4 |
	#				+-----------------+--------------+

# INSERTS para categorias
INSERT INTO categorias VALUES(null,'Fantasia');
INSERT INTO categorias VALUES(null,'Deportes');
INSERT INTO categorias VALUES(null,'Shoter');
INSERT INTO categorias VALUES(null,'Plataformas');

# INSERTS para entradas
	# usuario 1
INSERT INTO entradas VALUES(null,1,3,'GTA','review de GTA',CURDATE());
	#usuario 2
INSERT INTO entradas VALUES(null,2,1,'LOL','review LOL',CURDATE());
INSERT INTO entradas VALUES(null,2,2,'Moto Cross','como activar el turbo',CURDATE());
INSERT INTO entradas VALUES(null,2,4,'Mario Bros','review de Mario Bros',CURDATE());
	#usuario 3
INSERT INTO entradas VALUES(null,3,3,'FIFA-19','Nuevos jugadores en FIFA-19',CURDATE());
INSERT INTO entradas VALUES(null,3,4,'Zelda','Explicaion de niveles',CURDATE());

