# Insertando nuevos datos o registros
# usando Insert basico

INSERT INTO usuarios VALUES(null,'jack','ybarra','jack@mail.com','123','2019-09-08');

#usando Insert avanzado
#insertar filas con solo ciertas columnas
# este tipo de consulta solo funciona si no hay otros campos NOT NULL
INSERT INTO usuarios(email, password) VALUES('manuel@mail.com','321');
INSERT INTO entradas(descripcion) VALUES('Hello world everyone');
