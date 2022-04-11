import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir='./client/instantclient_19_8')

dsn_str = cx_Oracle.makedsn('140.117.69.58', '1521', 'ORCL')
connection = cx_Oracle.connect(
    user='group13',
    password='Group133',
    dsn=dsn_str
)