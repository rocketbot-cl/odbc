



# ODBC
  
Conecta a multiples base de datos con odbc.
  
![banner](imgs/Banner_odbc.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  




## Como usar este módulo
Para usar este módulo, tienes que tener instalados los dirvers correctos para la base de 
datos con la cual se desea interactuar.



## Descripción de los comandos

### Listar drivers odbc
  
Retorna una lista con todos los drivers odbc
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filter|Palabra para aplciar el filtro|Access|
|Asignar resultado a variable|Variable donde guardar el resultado.|Variable|

### Conectarse a Base de Datos
  
Comando para conectarse a una base de datos desde driver odbc
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione el driver|||
|Parámetros|Datos para la conexión.|SERVER=localhost;PORT=1433;DATABASE=mi_db|

### Ejecutar query
  
Ejecuta query en la base de datos conectada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Query|Query que se desea ejecutar.|select * from tabla|
|Parametros|Parametros necesarios, si es que son requeridos.|300,'test'|
|Asignar resultado a variable|Variable donde guardar el resultado.|Variable|

### Cerrar conexión
  
Cierra la conexión de odbc
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
