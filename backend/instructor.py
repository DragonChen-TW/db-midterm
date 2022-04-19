from .connect import connection
from .utils import *



def get_all_instructor():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM INSTRUCTOR''')
    
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

def insert_instructor(name, email, password):
    cursor = connection.cursor()

    instructors = get_all_instructor()
    max_id = max([int(i['I_ID']) for i in instructors])
    new_id = max_id + 1

    sql = f'''
        INSERT INTO instructor (I_ID, NAME, EMAIL, PASSWORD)
        VALUES ({new_id}, '{name}', '{email}', '{password}')
    '''

    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()

def insert_to_course(course):
    cursor = connection.cursor()
    
    sql = f'''
        INSERT INTO COURSE (COURSE_ID, TITLE, CATEGORY, BRIEF, COURSE_FEE, LANGUAGE)
        VALUES ({course['c_id']}, '{course['c_title']}', '{course['c_cate']}', '{course['c_brief']}', {course['c_fee']}, '{course['c_lang']}')
    '''
    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()

def edit_to_course(course_id, course):
    cursor = connection.cursor()
    
    sql = f'''
        UPDATE COURSE
        SET TITLE = '{course['c_title']}', BRIEF = '{course['c_brief']}', COURSE_FEE = '{course['c_fee']}', LANGUAGE = '{course['c_lang']}'
        WHERE COURSE_ID = {course_id}
    '''
    print('sql: ', sql)
    res = cursor.execute(sql)
    # connection.commit()

def insert_to_course_instructor(c_id, instructor_id):
    cursor = connection.cursor()
    
    sql = f'''INSERT INTO COURSEINSTRUCTOR (COURSE_ID, I_ID) VALUES ({c_id}, {instructor_id})'''
    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()

def insert_to_chapter(chapter):
    cursor = connection.cursor()
    print(f'chapter contents: {chapter}')

    sql = f'''
            INSERT INTO CHAPTER (CHAPTER_ID, CHAPTER_TITLE, COURSE_ID) 
            VALUES ({chapter['chapter_id']}, '{chapter['chapter_title']}', {chapter['course_id']})'''
    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()

def insert_to_content(content):
    cursor = connection.cursor()
    print(f'content contents: {content}')
    
    sql = f'''
            INSERT INTO CONTENT (CONTENT_ID, TYPE, IS_MANDATORY, REQUIRED_TIME, FILE_PATH, CHAPTER_ID) 
            VALUES (
                {content['content_id']}, '{content['type']}', {content['mandatory']}, 
                {content['required_time']}, '{content['file_path']}', {content['chapter_id']})'''

    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()
