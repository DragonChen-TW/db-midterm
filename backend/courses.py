from .connect import connection

def get_all_courses():
    cursor = connection.cursor()

    res = cursor.execute('''SELECT * FROM COURSE''')

    courses = res.fetchall()
    print('res', courses)
    return courses