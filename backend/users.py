from .connect import connection
from .utils import *

def insert_user(name, email, password):
    cursor = connection.cursor()

    users = get_all_students()
    max_id = max([int(u['S_ID']) for u in users])
    new_id = max_id + 1

    sql = f'''
        INSERT INTO student (S_ID, NAME, EMAIL, PASSWORD)
        VALUES ({new_id}, '{name}', '{email}', '{password}')
    '''

    print('sql: ', sql)
    res = cursor.execute(sql)
    connection.commit()

def login_verify(email, password):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM student WHERE email = '{email}' '''
    res = cursor.execute(sql)
    stu = res.fetchone()
    s_cols = parse_column_headers(res)

    sql = f'''SELECT * FROM instructor WHERE email = '{email}' '''
    res = cursor.execute(sql)
    ins = res.fetchone()
    i_cols = parse_column_headers(res)
    
    if not stu and not ins:
        return None

    stu = stu and dict(zip(s_cols, stu))
    ins = ins and dict(zip(i_cols, ins))

    print('stu', stu, 'ins', ins)
    
    # get the first entity out from one of two tables
    u = stu or ins

    if password != u['PASSWORD']:
        return False
    
    u.pop('PASSWORD', None)
    u.pop('REGISTER_DATE', None)

    return u

def get_all_students():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM STUDENT''')
    cols = parse_column_headers(res)
    users = [dict(zip(cols, r)) for r in res]

    return users

def get_all_snaps():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT COUNT(s_id) as numberOfStudents FROM  STUDENT''')
    cols = parse_column_headers(res)
    num_student = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT COUNT(i_id) as numberOfInsturctors FROM  INSTRUCTOR''')
    cols = parse_column_headers(res)
    num_insturctor = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT COUNT(course_id) as numberOfCourse FROM  COURSE''')
    cols = parse_column_headers(res)
    num_course = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''select category, COUNT(category) as numberOfCategory from COURSE group by category''')
    cols = parse_column_headers(res)
    num_category = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT *
    FROM COURSE c LEFT OUTER JOIN (
        SELECT c.COURSE_ID, AVG(star) AS avg_star, COUNT(star) AS population
        FROM COURSE c LEFT OUTER JOIN FEEDBACK f
        ON c.COURSE_ID = f.COURSE_ID
        GROUP BY c.COURSE_ID
    ) f
    ON c.COURSE_ID = f.COURSE_ID
    WHERE population > 1
    ORDER BY AVG_STAR DESC
    FETCH NEXT 3 ROWS ONLY''')
    cols = parse_column_headers(res)
    num_popular = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT *
    FROM COURSE
    ORDER BY course_id DESC
    FETCH NEXT 3 ROWS ONLY''')
    cols = parse_column_headers(res)
    num_newest = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT i.NAME, students_num
    FROM INSTRUCTOR i
    NATURAL JOIN
    (SELECT  I_ID, COUNT(*) as students_num
    FROM ENROLL
    NATURAL JOIN COURSEINSTRUCTOR
    GROUP BY I_ID)
    ORDER BY students_num DESC
    FETCH NEXT 3 ROWS ONLY''')
    cols = parse_column_headers(res)
    pop_instr = [dict(zip(cols, r)) for r in res]

    res = cursor.execute('''SELECT *
    FROM
    (SELECT name, title, review
    FROM FEEDBACK
    natural join course
    natural join student
    WHERE review IS NOT NULL)
    ORDER BY DBMS_RANDOM.value FETCH NEXT 4 ROWS ONLY''')
    cols = parse_column_headers(res)
    comment = [dict(zip(cols, r)) for r in res]

    return num_student, num_insturctor, num_course, num_category, num_popular, num_newest, pop_instr, comment

def get_student_detail(s_id):
    cursor = connection.cursor()

    sql = f'''SELECT * FROM STUDENT WHERE S_ID = '{s_id}' '''
    print('sql', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    u = dict(zip(cols, res.fetchone()))

    u.pop('PASSWORD', None)
    u.pop('REGISTER_DATE', None)

    # Add more detailed query about courses and 

    return u

def get_student_enroll_course(s_id):
    cursor = connection.cursor()

    sql = f'''SELECT C.* FROM ENROLL E, COURSE C WHERE S_ID = '{s_id}' AND E.COURSE_ID = C.COURSE_ID'''
    print('sql', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    u = [dict(zip(cols, r)) for r in res]
    print(u)

    return u

def get_student_enroll_payment(s_id):
    cursor = connection.cursor()

    sql = f'''SELECT C.TITLE, P.* FROM ENROLL E, PAYMENT P, COURSE C WHERE S_ID = '{s_id}' AND E.P_ID = P.P_ID AND E.COURSE_ID = C.COURSE_ID'''
    print('sql', sql)
    res = cursor.execute(sql)
    cols = parse_column_headers(res)
    u = [dict(zip(cols, r)) for r in res]
    print(u)

    return u