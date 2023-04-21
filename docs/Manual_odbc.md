



# ODBC
  
Use Open DataBase Connectivity to connect to and manage your database system.  

  
*Read this in other languages: [English](Manual_ODBC.md), [Português](Manual_ODBC.pr.md), [Español](Manual_ODBC.es.md)*  

  
![banner](imgs/Banner_odbc.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

In order to use this module, you need to have your database management system corresponding driver.

## Description of the commands

### List odbc drivers
  
Return an list with all odbc drivers
|Parameters|Description|example|
| --- | --- | --- |
|Filter|Word to apply in the filter|Access|
|Assign result to variable |Variable where to store the result.|Variable|

### Connect DB
  
Connect to db from odbc driver
|Parameters|Description|example|
| --- | --- | --- |
|Select driver|||
|Parameters|Data necessary for the connection.|SERVER=localhost;PORT=1433;DATABASE=mi_db|

### Execute query
  
Execute query to connected db
|Parameters|Description|example|
| --- | --- | --- |
|Query|Query you want to execute.|select * from table|
|Params|Params, if they are necessary.|300, 'test|
|Assign result to variable |Variable where to store the result.|Variable|

### Close connection
  
Close odbc connection
|Parameters|Description|example|
| --- | --- | --- |
