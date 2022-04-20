from flask import session
from .connect import connection
from .utils import *
from random import sample

def get_max5_feedbacks(course_id):
    cursor = connection.cursor()
    sql = f'''
        SELECT * FROM FEEDBACK NATURAL JOIN STUDENT
        WHERE COURSE_ID = {course_id}
    '''
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    feedbacks = [dict(zip(cols, r)) for r in res]

    if len(feedbacks) >= 5:
        feedbacks = sample(feedbacks, 5)

    return feedbacks

def get_my_feedback(course_id):
    s_id = session.get('user').get('s_id')
    if not s_id:
        return None

    cursor = connection.cursor()
    sql = f'''
        SELECT * FROM FEEDBACK NATURAL JOIN STUDENT
        WHERE COURSE_ID = {course_id} AND S_ID = {s_id}
    '''
    
    res = cursor.execute(sql).fetchone()
    if not res:
        return None
    feedback = dict(zip(cols, res.fetchone()))
    return feedback

def create_studentcontent(s_id, c_id):
    cursor = connection.cursor()

    sql = f'''
        INSERT INTO STUDENTCONTENT
        VALUES({s_id}, {c_id}, NULL, NULL, NULL)
    '''
    print('sql', sql)
    res = cursor.execute(sql)
    connection.commit()