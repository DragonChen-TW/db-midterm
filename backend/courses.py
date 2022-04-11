from .connect import connection
from .utils import *

def get_all_courses():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM COURSE''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses