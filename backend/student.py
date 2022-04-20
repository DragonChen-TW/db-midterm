from flask import session
from .connect import connection
from .utils import *
from datetime import datetime

def insert_to_enroll(enrollment):
	cursor = connection.cursor()
	
	sql_get = f'''
				SELECT COURSE_ID FROM ENROLL
				WHERE S_ID = {enrollment['s_id']}'''
	res_get = cursor.execute(sql_get)
	cols = parse_column_headers(res_get)

	# if no record 
	if res_get.fetchone() == None:
		sql = f'''      
		INSERT INTO ENROLL
		VALUES ({enrollment['course_id']}, {enrollment['s_id']}, NULL, to_date('{enrollment['e_date']}', 'YYYY-MM-DD'))
		'''
		res = cursor.execute(sql)
		connection.commit()
		print("Insert into ENROLL success!")
		return True
	else: 
		exist_courses = dict(zip(cols, res_get.fetchone()))

		if enrollment['course_id'] not in exist_courses:
			sql = f'''      
	    	INSERT INTO ENROLL
	    	VALUES ({enrollment['course_id']}, {enrollment['s_id']}, NULL, to_date('{enrollment['e_date']}', 'YYYY-MM-DD'))
	    	'''
			res = cursor.execute(sql)
			connection.commit()
			print("Insert into ENROLL success!")
			return True
		else:
			print("Insertion failed")
			return False


def check_studentcontent_exist(s_id, c_id):
    cursor = connection.cursor()

    sql = f'''
        SELECT * FROM STUDENTCONTENT
        WHERE S_ID = {s_id} AND CONTENT_ID = {c_id}
    '''
    res = cursor.execute(sql).fetchone()
    return res != None

def create_studentcontent(s_id, c_id):
    cursor = connection.cursor()

    sql = f'''
        INSERT INTO STUDENTCONTENT
        VALUES({s_id}, {c_id}, NULL, NULL, NULL)
    '''
    print('sql', sql)
    res = cursor.execute(sql)
    connection.commit()

def complete_or_cancel_content(c_id, complete=True):
    s_id = session.get('user').get('S_ID') # student ID
    cursor = connection.cursor()

    if not check_studentcontent_exist(s_id, c_id):  # if there is no record
        create_studentcontent(s_id, c_id)
    print('exist', check_studentcontent_exist(s_id, c_id))

    if complete: # set as complete
        sql = f'''
            UPDATE STUDENTCONTENT sc
            SET STATUS = 'finish', COMPLETE = TO_DATE('{datetime.now().replace(microsecond=0)}', 'YYYY-MM-DD HH24:MI:SS')
            WHERE sc.S_ID = {s_id} AND CONTENT_ID = {c_id}
        '''
    else:        # set as unfinished
        sql = f'''
            UPDATE STUDENTCONTENT sc
            SET STATUS = NULL, COMPLETE = NULL 
            WHERE sc.S_ID = {s_id} AND CONTENT_ID = {c_id}
        '''
    print('sql', sql)
    res = cursor.execute(sql)
    connection.commit()