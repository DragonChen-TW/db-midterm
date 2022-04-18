from .connect import connection
from .utils import *

def get_all_courses():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM COURSE''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses

def get_one_course(id):
    cursor = connection.cursor()
    # print(id)
    res = cursor.execute(f'''SELECT * FROM COURSE WHERE COURSE_ID = {id}''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses

def remove_one_course(c_id):
    cursor = connection.cursor()
    sql = f'''DELETE FROM COURSE WHERE COURSE_ID = {c_id} '''
    # print('sql', sql)
    res = cursor.execute(sql)
    connection.commit()

def get_courses_by_instructor(instructor_id):
    cursor = connection.cursor()
    print(instructor_id)
    
    res = cursor.execute(f'''SELECT * FROM COURSE C, COURSEINSTRUCTOR CI 
                                WHERE I_ID = '{instructor_id}' 
                                AND C.COURSE_ID = CI.COURSE_ID''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]
    print(courses)

    return courses

def get_course_chapter(c_id):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM CHAPTER WHERE COURSE_ID = {c_id}'''
    # print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    chapters = [dict(zip(cols, r)) for r in res]

    return chapters

def get_course_contents(c_id):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM (CONTENT NATURAL JOIN CHAPTER) LEFT OUTER JOIN STUDENTCONTENT ON CONTENT.CONTENT_ID = STUDENTCONTENT.CONTENT_ID WHERE COURSE_ID = {c_id}'''

    # sql = f'''SELECT CHAPTER_ID, CHAPTER_TITLE, FILE_PATH, REQUIRED_TIME, COUNT(S_ID) "S_AMOUNT", COUNT(S_ID WHEN STATUS='finish' THEN 1 END) "S_FINISH" FROM (CONTENT NATURAL JOIN CHAPTER) NATURAL JOIN STUDENTCONTENT WHERE COURSE_ID = {c_id} GROUP BY CONTENT_ID'''
    print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    contents = [dict(zip(cols, r)) for r in res]

    contents = sorted(contents, key=lambda d: d['CHAPTER_ID']) 

    return contents