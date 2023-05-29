



# ODBC
  
Utiliza Open DataBase Connectivity para conectarte y gestionar tu sistema de bases de datos.  

  
*Read this in other languages: [English](Manual_ODBC.md), [Português](Manual_ODBC.pr.md), [Español](Manual_ODBC.es.md)*  


## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este módulo
Para usar este módulo, tienes que tener instalados los dirvers correctos para la base de datos con la cual se desea interactuar.



## Overview


1. Listar drivers odbc  
Retorna una lista con todos los drivers odbc

2. Conectarse a Base de Datos  
Comando para conectarse a una base de datos desde driver odbc

3. Ejecutar query  
Ejecuta query en la base de datos conectada

4. Cerrar conexión  
Cierra la conexión de odbc  




----
### OS

- windows

### Dependencies
- [**pyodbc**](https://pypi.org/project/pyodbc/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)