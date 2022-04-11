from .connect import connection
from .utils import *

def get_all_students():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM STUDENT''')
    cols = parse_column_headers(res)
    users = [dict(zip(cols, r)) for r in res]

    return users