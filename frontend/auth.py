from flask import (
    Blueprint, render_template,
    redirect, flash,
    request, session
)
from backend.users import get_all_students, verify_student_password, get_student_detail, get_student_enroll_course, get_student_enroll_payment

# Can call `flash(msg_text, alert_type)` to show a temporary message on page
# alert_type could be 'success', 'danger', 'info', etc.
# View https://getbootstrap.com/docs/5.1/components/alerts/#link-color to get all the types

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
        pwd = request.form.get('password') # 抓取 form.html 中 input text 的值

        user = verify_student_password(email, pwd)

        if user == None:
            flash('查無此用戶資訊，請先註冊帳號', 'danger')
        elif user == False:
            flash('密碼輸入錯誤，請重新檢查', 'danger')
        else:
            session['user'] = user
            # Login success, redirect
            flash('登入成功', 'success')
            return redirect('/')
    return render_template('auth/login.html')

@auth_app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    flash('登出成功', 'success')
    return redirect('/')

@auth_app.route('/user/<user_id>')
def show_student_profile(user_id):
    print('u_id', user_id)
    u = get_student_detail(user_id)

    print('profile', u)

    return render_template('auth/student_profile.html', user=u)

@auth_app.route('/user/<user_id>/mycourse')
def show_student_course(user_id):
    print('u_id', user_id)
    u = get_student_enroll_course(user_id)

    print('course', u)

    return render_template('auth/student_course.html', user=u)

@auth_app.route('/user/<user_id>/mypayment')
def show_student_payment(user_id):
    print('u_id', user_id)
    u = get_student_enroll_payment(user_id)

    print('payment', u)

    return render_template('auth/student_payment.html', user=u)