from .connect import connection
from .utils import *

def get_all_courses():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM COURSE''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses

def get_one_courses(id):
    cursor = connection.cursor()
    print(id)
    res = cursor.execute(f'''SELECT * FROM COURSE WHERE COURSE_ID = {id}''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses