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
        self.__connection = self.pyodbc.connect(**value)


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
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e


if module == "connect":
    driver = GetParams('driver')
    params = GetParams("params")

    if driver not in pyodbc.drivers():
        raise Exception(f"{driver} not exists in driver list")

    try:

        args = {"driver": driver}
        if params.startswith("{"):
            params = eval(params)
            for key in params:
                args[key] = params[key]
        elif params is not None or params != "":
            for param in params.split(";"):
                key_value = param.split("=")
                args[key_value[0]] = key_value[1]

        odbc_mod = OdbcModule(args, pyodbc)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "execute_query":

    def query2params(*args):
        queries = []
        print(args)
        for param in args:
            if param.startswith("to_date"):
                p = datetime.strptime(date_, format_)
                queries.append(p)
            else:
                queries.append(param)
        return tuple(queries)
    try:
        query = GetParams('query')
        result = GetParams('var_')
        params = GetParams('params')
        cursor = conn.cursor()

        if query.lower().startswith(('{call', '{ call')):
            params = tuple(params.split(","))
            q = (query, ) + query2params(*params)
            cursor.execute(*q)
        else:
            cursor.execute(query)

        if query.lower().startswith(('select', '{call', '{ call')):
            row = cursor.fetchone()
            if row:
                print(row[0])
                # data = []
            # # print(query)
            # # data.append(columns)
            # for row in cursor.fetchall():
            #     # print(row)
            #     ob_ = []
            #     for r in row:
            #         ob_.append(str(r) + "")
            #     data.append(ob_)
        else:
            conn.commit()
            data = cursor.rowcount, 'registros afectados'
        conn.commit()
        SetVar(result, data)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e
