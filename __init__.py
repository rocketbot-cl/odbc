# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Función que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'odbc' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import pyodbc

global odbc_mod

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Automate Android devices
"""


class OdbcModule:
    def __init__(self, parameters, odbc):
        self.pyodbc = odbc
        self.connection = parameters

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = self.pyodbc.connect(value)


if module == "listDrivers":
    result = GetParams('result')
    filter_ = GetParams('filter')
    try:
        drivers = []
        for driver in pyodbc.drivers():
            if bool(filter_):
                if filter_ in driver:
                    drivers.append(driver)
            else:
                drivers.append(driver)

        SetVar(result, drivers)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e


if module == "connect":
    driver = GetParams('driver')
    params = GetParams("params")

    if driver not in pyodbc.drivers():
        raise Exception(f"{driver} not exists in driver list")

    try:

        driver = "{" + driver + "}"
        params = "" if params is None else params
        conn_str = f'Driver={driver};' + params

        odbc_mod = OdbcModule(conn_str, pyodbc)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "execute_query":
    try:
        query = GetParams('query')
        result = GetParams('var_')

        cursor = odbc_mod.connection.cursor()
        cursor.execute(query)

        fetch = cursor.fetchall()
        if result:
            SetVar(result, fetch)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e
