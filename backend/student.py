from .connect import connection
from .utils import *

def insert_to_enroll(enrollment):
	cursor = connection.cursor()
	
	sql_get = f'''
				SELECT COURSE_ID FROM ENROLL
				WHERE S_ID = {enrollment['s_id']}'''
	res_get = cursor.execute(sql_get)
	cols = parse_column_headers(res_get)
	print(f"fetch one: {res_get.fetchone()}")

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

	