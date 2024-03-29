from flask import session
import datetime
from .connect import connection
from .utils import *

def get_all_courses():
    cursor = connection.cursor()

    res = cursor.execute('''
    SELECT *
    FROM COURSE c LEFT OUTER JOIN (
        SELECT c.COURSE_ID, AVG(star) AS avg_star, COUNT(star) AS population
        FROM COURSE c LEFT OUTER JOIN FEEDBACK f
        ON c.COURSE_ID = f.COURSE_ID
        GROUP BY c.COURSE_ID
    ) f
    ON c.COURSE_ID = f.COURSE_ID
    ORDER BY c.COURSE_ID
    ''')
    
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    print('courses', courses)
    for i, c in enumerate(courses):
        if not c['AVG_STAR']:
            courses[i]['AVG_STAR'] = 0

    return courses

def get_all_courses_search(course_tmp):
    cursor = connection.cursor()
    print(course_tmp)
    
    conditions = []
    if course_tmp.get('c_title'):
        conditions.append(f"TITLE like '%{course_tmp['c_title']}%'")
    if course_tmp.get('c_cate'):
        conditions.append(f"CATEGORY like '%{course_tmp['c_cate']}%'")
    if course_tmp.get('c_lang'):
        conditions.append(f"LANGUAGE like '%{course_tmp['c_lang']}%'")
    conditions = " AND ".join(conditions)
    conditions = f'WHERE {conditions}'

    sql = f'''
    SELECT *
    FROM COURSE c LEFT OUTER JOIN (
        SELECT c.COURSE_ID, AVG(star) AS avg_star, COUNT(star) AS population
        FROM COURSE c LEFT OUTER JOIN FEEDBACK f
        ON c.COURSE_ID = f.COURSE_ID
        GROUP BY c.COURSE_ID
    ) f
    ON c.COURSE_ID = f.COURSE_ID
    {conditions}
    ORDER BY c.COURSE_ID
    '''
    res = cursor.execute(sql)
    
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    print('courses', courses)
    for i, c in enumerate(courses):
        if not c['AVG_STAR']:
            courses[i]['AVG_STAR'] = 0

    return courses

def get_one_course(id):
    cursor = connection.cursor()
    # print(id)
    res = cursor.execute(f'''SELECT * FROM COURSE WHERE COURSE_ID = {id}''')
    cols = parse_column_headers(res)
    course = dict(zip(cols, res.fetchone()))

    res = cursor.execute(f'''SELECT name
    FROM COURSE c, INSTRUCTOR i, courseinstructor ci  
    WHERE c.COURSE_ID = {id} AND c.course_id = ci.course_id AND i.i_id = ci.i_id''')
    cols = parse_column_headers(res)
    instr_name = [dict(zip(cols, r)) for r in res]
    course['INSTR_NAME'] = instr_name

    return course

def remove_one_course(c_id):
    cursor = connection.cursor()
    sql = f'''DELETE FROM COURSE WHERE COURSE_ID = {c_id} '''
    print('sql', sql)
    res = cursor.execute(sql)
    connection.commit()


def get_courses_by_instructor(instructor_id):
    cursor = connection.cursor()
    
    res = cursor.execute(f'''
        SELECT * FROM COURSE C, COURSEINSTRUCTOR CI 
        WHERE CI.I_ID = '{instructor_id}' 
        AND C.COURSE_ID = CI.COURSE_ID
        ORDER BY C.COURSE_ID
    ''')
    cols = parse_column_headers(res)
    courses = [dict(zip(cols, r)) for r in res]

    return courses

def get_course_chapter(c_id):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM CHAPTER WHERE COURSE_ID = {c_id}'''
    # print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    chapters = [dict(zip(cols, r)) for r in res]

    return chapters

def get_all_chapters():
    cursor = connection.cursor()
    sql = f'''
            SELECT * FROM CHAPTER
            '''
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    chapters = [dict(zip(cols, r)) for r in res]

    chapters = sorted(chapters, key=lambda d: d['CHAPTER_ID']) 

    return chapters

def get_all_contents():
    cursor = connection.cursor()
    sql = f'''
            SELECT * FROM CONTENT
            '''
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    contents = [dict(zip(cols, r)) for r in res]

    contents = sorted(contents, key=lambda d: d['CONTENT_ID']) 

    return contents

def get_course_contents(c_id):
    cursor = connection.cursor()

    sql = f'''
        SELECT * FROM (CONTENT NATURAL JOIN CHAPTER)
        WHERE COURSE_ID = {c_id}
    '''

    print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    contents = [dict(zip(cols, r)) for r in res]

    contents = sorted(contents, key=lambda d: d['CHAPTER_ID']) 

    return contents

def get_student_course_contents(c_id):
    s_id = session.get('user').get('S_ID') # student ID

    cursor = connection.cursor()

    sql = f'''
        SELECT * FROM 
            (CHAPTER ch JOIN CONTENT co ON ch.CHAPTER_ID = co.CHAPTER_ID)
            LEFT OUTER JOIN (
                SELECT S_ID, CONTENT_ID AS SC_C_ID, COMPLETE, STATUS
                FROM STUDENTCONTENT sc WHERE sc.S_ID = {s_id}
            ) sc
            ON co.CONTENT_ID = sc.SC_C_ID
        WHERE COURSE_ID = {c_id}
        ORDER BY ch.CHAPTER_ID, co.CONTENT_ID
    '''

    print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    contents = [dict(zip(cols, r)) for r in res]
    
    print('contents', contents)

    return contents

def get_course_chapters(course_id):
    cursor = connection.cursor()

    sql = f'''
        SELECT * FROM CHAPTER
        WHERE COURSE_ID = {course_id}
    '''

    print('sql: ', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    chapters = [dict(zip(cols, r)) for r in res]

    chapters = sorted(chapters, key=lambda d: d['CHAPTER_ID']) 

    return chapters

def check_exist_chapter(title, course_id):
    cursor = connection.cursor()
    sql = f'''
            SELECT CHAPTER_ID FROM CHAPTER
            WHERE CHAPTER_TITLE = '{title}' AND COURSE_ID = {course_id}
            '''    
    print(f'sql: {sql}')
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    chapters = [dict(zip(cols, r)) for r in res]

    
    print(f'result of check exist chapter: {chapters}')

    if len(chapters) < 1:
        return None
    else: 
        return chapters

def remove_one_content(content_id):
    cursor = connection.cursor()
    sql = f'''DELETE CONTENT WHERE CONTENT_ID = {content_id}'''
    print(f'sql: {sql}')
    res = cursor.execute(sql)
    connection.commit()

def get_one_content(content_id):
    cursor = connection.cursor()
    # print(id)
    res = cursor.execute(f'''SELECT * FROM CONTENT WHERE CONTENT_ID = {content_id}''')
    cols = parse_column_headers(res)
    content = dict(zip(cols, res.fetchone()))

    return content
