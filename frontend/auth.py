from flask import (
    Blueprint, render_template,
    redirect,
    request, session
)
from backend.users import get_all_students, verify_student_password

auth_app = Blueprint('auth_app', __name__)

@auth_app.route('/')
def show_all_students():
    students = get_all_students()
    print('stu', students)
    return render_template('auth/user_list.html', students=students)

@auth_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        pwd = request.form.get('password') # 抓取form.html中input text的值

        check = verify_student_password(email, pwd)

        if check == None:
            failed_notify = '查無此用戶資訊，請先註冊帳號'
            return render_template('auth/login.html', failed_notify=failed_notify)
        elif check == False:
            failed_notify = '密碼輸入錯誤，請重新檢查'
            return render_template('auth/login.html', failed_notify=failed_notify)
        else:
            success_notify = '登入成功'
            session['email'] = email
            session['name'] = check['NAME']
            session['user_type'] = 'student'

            # Login success, redirect
            return redirect('/')
    return render_template('auth/login.html')

@auth_app.route('/logout', methods=['GET'])
def logout():
    session.pop('email', None)
    session.pop('name', None)
    session.pop('user_type', None)

    return redirect('/')