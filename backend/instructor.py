from .connect import connection
from .utils import *



def get_all_instructor():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT NAME, REGISTER_DATE, INTRODUCTION_BRIEF FROM INSTRUCTOR''')
    
    cols = parse_column_headers(res)
    instructor = [dict(zip(cols, r)) for r in res]

    return instructor

def get_instructor_detail(instructor_id):
    cursor = connection.cursor()
    sql = f'''SELECT * FROM instructor WHERE I_ID = '{instructor_id}' '''
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    u = dict(zip(cols, res.fetchone()))

    u.pop('PASSWORD', None)
    u.pop('REGISTER_DATE', None)

    # Add more detailed query about courses and 

    return u

def insert_to_course(course):
    cursor = connection.cursor()
    
    sql = f'''INSERT INTO COURSE (COURSE_ID, TITLE, CATEGORY, BRIEF, COURSE_FEE, LANGUAGE) VALUES ({course['c_id']}, '{course['c_title']}', '{course['c_cate']}', '{course['c_brief']}', {course['c_fee']}, '{course['c_lang']}')'''
    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()


def insert_to_course_instructor(c_id, instructor_id):
    cursor = connection.cursor()
    
    sql = f'''INSERT INTO COURSEINSTRUCTOR (COURSE_ID, I_ID) VALUES ({c_id}, {instructor_id})'''
    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()