from .connect import connection
from .utils import *

def login_verify(email, password):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM student WHERE email = '{email}' '''
    res = cursor.execute(sql)
    stu = res.fetchone()
    s_cols = parse_column_headers(res)

    sql = f'''SELECT * FROM instructor WHERE email = '{email}' '''
    res = cursor.execute(sql)
    ins = res.fetchone()
    i_cols = parse_column_headers(res)
    
    if not stu and not ins:
        return None

    stu = stu and dict(zip(s_cols, stu))
    ins = ins and dict(zip(i_cols, ins))

    print('stu', stu, 'ins', ins)
    
    # get the first entity out from one of two tables
    u = stu or ins

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