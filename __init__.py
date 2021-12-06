# coding: utf-8
"""
Base for development of external modules.

To get the data sent by the robot this function is used:
    GetParams()

To get the module or function that is being called:
    GetParams("module")

To get variable sent from Rocketbot command or form:
    var = GetParams("id")
    The "id" are defined in forms of the package.json file

To modify a Rocketbot variable:
    SetVar("name", "dato")

To get a Rocketbot variable:
    var = GetVar(Variable_Rocketbot)

To get selected option:
    opcion = GetParams("option")

To install libraries you must enter the module folder by terminal.
    pip install <package> -t .\libs

"""

# Python libraries
import os
import sys

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'odbc' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

# Import external libraries
import pyodbc

"""
The code of each module works as a local scope. Each command that is executed resets the data.
To share information between commands, declare the variable as global. The sintax will be 'mod_modulename' or similar
"""

global mod_odbc_sessions

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"
try:
    if not mod_odbc_sessions :
        mod_odbc_sessions = {SESSION_DEFAULT:{}}
except NameError:
    mod_odbc_sessions = {SESSION_DEFAULT:{}}


# Get data from robot
module = GetParams("module") # Get command executed
session = GetParams("session") # Get Session name
if not session:
    session = SESSION_DEFAULT

try:
    if module == "get_drivers":
        var_name = GetParams("var_name")
        print(var_name)
        SetVar(var_name, {
            "drivers": pyodbc.drivers()
        })

    if module == "listDrivers":
        result = GetParams('result')
        filter_ = GetParams('filter')

        drivers = []
        for driver in pyodbc.drivers():
            if bool(filter_):
                if filter_ in driver:
                    drivers.append(driver)
            else:
                drivers.append(driver)

        SetVar(result, drivers)

    if module == "connect":
        driver = GetParams('driver') # Compatibility with v1.1
        params = GetParams("params")
        iframe = GetParams("iframe")

        if not driver:
            driver = eval(iframe)["driver"]

        if driver not in pyodbc.drivers():
            raise Exception(f"{driver} not exists in driver list")

        args = {"driver": driver}

        if params is None:
            params = {}

        elif params.startswith("{"):
            params = eval(params)

        elif ";" in params:
            params = {param.split("=")[0]: param.split("=")[1] for param in params.split(";")}

        args.update(params)
        odbc_mod = pyodbc.connect(**args)
        mod_odbc_sessions[session] = odbc_mod


    if module == "execute_query":
        from mod_odbc import query2params

        query = GetParams('query')
        result = GetParams('var_')
        params = GetParams('params')

        connection = mod_odbc_sessions[session]
        cursor = connection.cursor()

        if params and params.startswith('['):
            params = tuple(eval(params))
        elif params:
            params = tuple(params.split(","))

        if query.lower().startswith(('{call', '{ call')) and params:
            # params = tuple(params.split(","))
            query_params = query2params(*params)
            q = (query, ) + query2params(*params)
            cursor.execute(*q)
        else:
            cursor.execute(query)
            
        data = []
        if query.lower().startswith(('select','execute', '{call')) and cursor.description:
            
                columns = [column[0] for column in cursor.description]

                for row in cursor:
                    ob_ = {}
                    t = 0
                    for r in row:
                        ob_[columns[t]] = str(r) + ""
                        t = t + 1

                    data.append(ob_)
        else:
            connection.commit()
            data = cursor.rowcount, 'registros afectados'

        connection.commit()
        SetVar(result, data)

    if module == 'closeConn':
        connection = mod_odbc_sessions[session]
        connection.close()


except Exception as e:
    print("\x1B[" + "31;40mError\x1B[" + "0m")
    PrintException("error")
    raise e
