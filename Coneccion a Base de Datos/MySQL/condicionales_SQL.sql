# Condicionales y otra clausulas:

# Condicional: WHERE

# ejemplo 1: con WHERE
SELECT * FROM usuarios WHERE email='jack@mail.com';

# ejemplo 2:
# 1. mostrar nombre y apellido de todos los usuarios registrados en 2019
SELECT nombre, apellido FROM usuarios WHERE YEAR(fecha)=2019;

# ejemplo 3; con operadores:
      # mostrar los nombres y apellidos diferentes a 2019 y que son Null o nulos.
SELECT nombre, apellido FROM usuarios WHERE YEAR(fecha)!=2019 OR ISNULL(fecha); 

# ejemplo 4: usando COMODINES con LIKE
      # usuarios en los que el apellido contenga a y contraseña sea 1234
SELECT email FROM usuarios WHERE apellidos LIKE '%a%' AND password='123'; 

# ejemplo 5
      # todos los usuarios registrados en año par
SELECT * FROM usuarios WHERE (YEAR(fecha)%2=0);

# ejemplo 6

SELECT UPPER(nombre), apellidos FROM usuarios WHERE LENGTH(nombre)>5 AND YEAR(fecha) > 2020;

# ejemplo 7: usando ORDER BY
      # ordenar todos los usuarios por el id Ascendentemente
SELECT * FROM usuarios ORDER BY id ASC;
      # ordenar todos los usuarios por el id Descendentemente
SELECT * FROM usuarios ORDER BY id DESC;
      # ordenar todos los usuarios por la fecha (automaticamente los ordena Ascendentemente)
SELECT * FROM usuarios ORDER BY fecha;

# ejemplo 8: Mostrar todo hasta cierto limite.
      #  muestra cierta cantidad de datos.

SELECT * FROM usuarios LIMIT 3;


/*
Consulta con condicionales::
    OPERADORES DE COMPARACION:
      igual                 =
      distinto              !=
      menor                 <
      mayor                 >
      menor o igual         <=
      mayor o igual         >=
      entre                 between
      en                    in
      es nulo               is null
      no nulo               is not null
      como                  like
      no es como            not like
*/
/*
COMODINES con LIKE
%     cualquier cantidad de caracteres

*/