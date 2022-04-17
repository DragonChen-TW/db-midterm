from .connect import connection
from .utils import *

def verify_student_password(email, password):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM student WHERE email = '{email}' '''
    print('sql', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)

    u = res.fetchone()
    if not u:
        return None

    u = dict(zip(cols, u))
    print('u', u)

    if password != u['PASSWORD']:
        return False
    
    u.pop('PASSWORD', None)
    u.pop('REGISTER_DATE', None)

    return u

def get_all_students():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM STUDENT''')
    cols = parse_column_headers(res)
    users = [dict(zip(cols, r)) for r in res]

    return users

def get_student_detail(s_id):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM STUDENT WHERE S_ID = '{s_id}' '''
    print('sql', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    u = dict(zip(cols, res.fetchone()))

    u.pop('PASSWORD', None)
    u.pop('REGISTER_DATE', None)

    # Add more detailed query about courses and 

    return u