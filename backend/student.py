from flask import session
from .connect import connection
from .utils import *
from datetime import datetime

def insert_to_enroll(enrollment):
	cursor = connection.cursor()
	
	sql_get = f'''
		SELECT COURSE_ID FROM ENROLL
		WHERE S_ID = {enrollment['s_id']} AND COURSE_ID = {enrollment['course_id']}
	'''
	res_get = cursor.execute(sql_get)
	cols = parse_column_headers(res_get)

	enroll = res_get.fetchone()

	# if no record 
	if enroll:
		print('You have enrolled this course')
		return False
	else:
		sql = f'''      
		INSERT INTO ENROLL
		VALUES ({enrollment['course_id']}, {enrollment['s_id']}, NULL, to_date('{enrollment['e_date']}', 'YYYY-MM-DD'))
		'''
		res = cursor.execute(sql)
		connection.commit()
		print("Insert into ENROLL success!")
		return True


def insert_to_studentcontent(student_content):
	cursor = connection.cursor()
	now = datetime.now()
	regist_time = now.strftime('%d-%m-%Y %H:%M:%S')
	print(f'register time: {regist_time}')

	sql_get = f'''
        SELECT * FROM STUDENTCONTENT
        WHERE S_ID = {student_content['s_id']} AND CONTENT_ID = {student_content['content_id']}
    '''
	res_get = cursor.execute(sql_get)
	cols = parse_column_headers(res_get)

	student_content = res_get.fetchone()

	# if no record, then insert new one
	if not student_content:
		sql = f'''      
		INSERT INTO STUDENTCONTENT
		VALUES ({student_content['s_id']}, {student_content['content_id']}, 
				TO_TIMESTAMP('{regist_time}', 'DD-MM-YYYY HH24:MI:SS'), NULL, 'not yet')
		'''
		res = cursor.execute(sql)
		connection.commit()
		print("Insert into ENROLL success!")
		return True
	else: 
		print("Already existed!")
		return False

def update_to_studentcontent(student_content):
	cursor = connection.cursor()
	now = datetime.now()
	regist_time = now.strftime('%d-%m-%Y %H:%M:%S')
	print(f'register time: {regist_time}')

	sql_get = f'''
        SELECT * FROM STUDENTCONTENT
        WHERE S_ID = {student_content['s_id']} AND CONTENT_ID = {student_content['content_id']}
    '''
	res_get = cursor.execute(sql_get)
	cols = parse_column_headers(res_get)
	
	stu_content = res_get.fetchone()

	# if no record, then insert new one
	if not stu_content:
		print("No record found")
		return False

	stu_content = dict(zip(cols, stu_content))

	if stu_content['STATUS'] == 'not yet':
		sql = f'''
			UPDATE STUDENTCONTENT
			SET STATUS = 'finish', COMPLETE = TO_TIMESTAMP('{regist_time}', 'DD-MM-YYYY HH24:MI:SS')
			WHERE S_ID = {student_content['s_id']} AND CONTENT_ID = {student_content['content_id']}
		'''
		res = cursor.execute(sql)
		connection.commit()
		return True
	else: 
		print("Already existed!")
		return False