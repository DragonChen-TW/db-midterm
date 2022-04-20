import cx_Oracle
import platform

p = platform.platform()
if p.startswith('darwin') or p.startswith('macOS'):
    cx_Oracle.init_oracle_client(lib_dir='./client/instantclient_19_8')


dsn_str = cx_Oracle.makedsn('140.117.69.58', '1521', 'ORCL')
connection = cx_Oracle.connect(
    user='group13',
    password='Group133',
    dsn=dsn_str
)
