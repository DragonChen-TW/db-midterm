import os
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir='./client/instantclient_19_8')

dsn_str = cx_Oracle.makedsn('140.117.69.58', '1521', 'ORCL')
connection = cx_Oracle.connect(
    user='group13',
    password='Group133',
    dsn=dsn_str
)

cursor = connection.cursor()

def run_sql_file(f_name):
    with open(f_name) as f:
        sqls = f.read().replace('\n', ' ')
        sqls = sqls.split(';')
        for sql in sqls:
            if '-- ' in sql:
                continue
            print('sql', sql[:50])
            try:
                cursor.execute(sql)
            except Exception as e:
                print('-----> error: ', e)
        connection.commit()

run_sql_file('backend/init.sql')
run_sql_file('backend/insert.sql')