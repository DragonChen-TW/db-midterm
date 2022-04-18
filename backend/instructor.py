from .connect import connection
from .utils import *

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