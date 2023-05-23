from datetime import datetime

def query2params(*args):
    queries = []
    print(args)
    for param in args:
        if str(param).startswith("to_date"):
            p = datetime.strptime(date_, format_)
            queries.append(p)
        else:
            queries.append(param)
    return tuple(queries)
