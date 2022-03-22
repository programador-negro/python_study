/* Crear lass tres tablas segun la imagen del diseño de base de datos

+ para crear las primary key, se usa al final de la tabla lo siguiente:
	CONSTRAINT pk_'nombre_de_tabla' PRIMARY KEY('nombre_del_campo')

+ para crear las foreign key, se al final de la tabla lo siguiente:
	CONSTRAINT fk_'asignar_cualquier_nombre' FOREIGN KEY('nombre_del_campo') REFERENCES 'nombre_de_tabla'('nombre_del_campo_con_que_va_conectado')
*/

CREATE TABLE usuarios(
id int(255) auto_increment not null,
nombre varchar(100) not null,
apellidos varchar(100) not null,
email varchar(255) not null,
password varchar(255) not null,
fecha date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;
/* ENGINE=InnoDb - da mayor de procesamiento he integridad  en los datos*/

CREATE TABLE entradas(
id int(255) auto_increment not null,
usuario_id int(255) not null,
categoria_id int(255) not null,
titulo varchar(255) not null,
descripcion MEDIUMTEXT,
fecha date not null,
CONSTRAINT pk_entradas PRIMARY KEY(id),
CONSTRAINT fk_entrada_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
CONSTRAINT fk_entrada_categoria FOREIGN KEY(categoria_id) REFERENCES categorias(id)
);


CREATE TABLE categorias(
id  int(255) auto_increment not null,
nombre varchar(100),
CONSTRAINT pk_categorias PRIMARY KEY(id)
);

