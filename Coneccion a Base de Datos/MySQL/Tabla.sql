/*
	PRUEBA MySQL: Creando una tabla.
	------
	Tipos de variables en MySQL:
	int(n° cifras)										ENTERO
	integer(n° cifras)								ENTERO
	varchar(n° caracteres) 						STRING
	char(n° caracteres)								STRING
	float(n° cifras, o, n° decimales)		DECIMAL
	date
	
	// para almacenar datos string grandes
	text	65535 caracteres
	mediumtext 16 millones caracteres
	longtext 4 billoes caracteres
	
	// para almacenar int grandes
	mediumint
	bigint
	
	// Restricciones de integridad basicas:
	not null		- importante, que no puede quedar vacio
	null		- no importante, que puede quedar vacio
	default 'xx'		-aparace un valor por defecto
	auto_increment		-va aumentando automaticamente por cada usuario o grupo de datos
		CONSTRAINT pk_(nombre_de_la_tabla) PRIMARY KEY(nombre_del_campo)
		importante colocar lo anterior ppara crear datos auto incrementales

*/

/* Creando una tabla - ejemplo 1 */
CREATE TABLE usuarios (
id int(11) auto_increment not null,
nombre varchar(100) not null,
apellidos varchar(100) default 'Ybarra',
email varchar(100) not null,
password varchar(255) not null,
CONSTRAINT pk_productos PRIMARY KEY(id)
);

/* Creando una tabla - ejemplo 2 */
CREATE TABLE productos(
id int(10) not null,
nombre varchar(255) not null
);
 /*
IMṔORTANTE:
- definir el tipo de dato y su logitud de caracteres (ej:varchar(255), int(11), float(N° de cifras, n° de decimales))
-  colocar NOT NULL si el campo se debe completar o NULL si se puede dejar en blanco.
 */

 