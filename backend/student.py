from .connect import connection
from .utils import *

def insert_to_enroll(enrollment):
    cursor = connection.cursor()

    print(f'enrollment: {enrollment}')
    sql = f'''      
            INSERT INTO ENROLL
            VALUES ({enrollment['course_id']}, {enrollment['s_id']}, NULL, to_date('{enrollment['e_date']}', 'YYYY-MM-DD'))
            '''
    print(f'sql: {sql}')
    res = cursor.execute(sql)
    connection.commit()