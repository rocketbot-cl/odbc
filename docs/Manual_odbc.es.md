



# ODBC
  
Utiliza Open DataBase Connectivity para conectarte y gestionar tu sistema de bases de datos.  

  
*Read this in other languages: [English](Manual_ODBC.md), [Português](Manual_ODBC.pr.md), [Español](Manual_ODBC.es.md)*  

  
![banner](imgs/Banner_odbc.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Como usar este módulo

Para utilizar este módulo, debe tener el controlador correspondiente de su sistema de administración de base de datos.

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
