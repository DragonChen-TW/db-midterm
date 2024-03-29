from datetime import date, datetime
from imp import is_builtin
from os import system
import time
import hashlib
from flask import (
    current_app,
    Blueprint, render_template,
    redirect, flash,
    request, session
)
from backend.users import (
    login_verify, 
    get_all_snaps,
    get_all_students, get_student_detail,
    get_student_enroll_course, get_student_enroll_payment,
    insert_user
)
from backend.instructor import insert_instructor
from backend.mail import send_mail
from backend.student import insert_to_enroll
from backend.courses import get_one_course

# Can call `flash(msg_text, alert_type)` to show a temporary message on page
# alert_type could be 'success', 'danger', 'info', etc.
# View https://getbootstrap.com/docs/5.1/components/alerts/#link-color to get all the types

auth_app = Blueprint('auth_app', __name__)

@auth_app.route('/')
def show_snaps():
    num_student, num_insturctor, num_course, num_category, num_popular, num_newest, pop_instr, comment = get_all_snaps()
    print(num_student, num_insturctor, num_course, num_category, num_popular)
    return render_template('home/homepage.html', num_student=num_student, num_insturctor=num_insturctor, 
    num_course=num_course, num_category=num_category, num_popular=num_popular, num_newest=num_newest, 
    pop_instr=pop_instr, comment=comment)

@auth_app.route('/contact')
def show_contact():
    return render_template('home/contact.html')

@auth_app.route('/about')
def show_about():
    return render_template('home/about.html')

@auth_app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_type = request.values.get('user_type')
        name = request.values.get('name')
        email = request.values.get('email')
        pwd = request.values.get('password')
        repeated_pwd = request.values.get('repeat_password')
        print(email, pwd, repeated_pwd)

        # test user exist
        u = login_verify(email, '')
        if u != None: # user exists
            flash('此 email 已註冊', 'danger')
        elif pwd != repeated_pwd:
            flash('請檢查兩次密碼是否相同', 'danger')
        else:
            # # generate hash
            key = f'{email} {time.time()}'
            value = hashlib.sha256(key.encode()).hexdigest()

            if user_type == 'Student':
                insert_user(name, email, pwd)
            elif user_type == 'Instructor':
                insert_instructor(name, email, pwd)
            else:
                flash(f'註冊失敗！不允許 user_type = {user_type} ', 'danger')
                return redirect('/sign_up')

            msg_title = f'歡迎您註冊本系統'
            msg_sender = ('DB 期中 Group 13', 'testcodepython1126@gmail.com')
            msg_receiver = [email] # TODO: to variable
            msg_content = f''

            with current_app.app_context():
                print('send')
                send_mail(
                    msg_title, msg_sender, msg_receiver, msg_content,
                    confirm_url=f'{request.url_root}/confirm?value={value}',
                    name=name,
                )
            
            flash('註冊成功，請至信箱完成驗證', 'success')
            return redirect('/login')
    
    return render_template('auth/sign_up.html')

@auth_app.route('/confirm', methods=['GET'])
def confirm_registraion():
    value = request.values.get('value')

    flash('驗證成功！歡迎註冊本系統', 'success')
    return redirect('/login')


@auth_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        pwd = request.form.get('password') # 抓取 form.html 中 input text 的值

        user = login_verify(email, pwd)
        # Get student entity or insturcotr entity
        # Student: {'S_ID': 4, 'NAME': 'goodgood', 'EMAIL': 'g23523@gmail.com'}
        # Instructor: {'I_ID': 2, 'NAME': 'dragon', 'EMAIL': 's123532@gmail.com', 'INTRODUCTION_BRIEF': '你好我是龍'}

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

@auth_app.route('/user/mycourse')
def show_student_course():
    user = session.get('user')
    if not user:
        flash('請先登入', 'danger')
        return redirect('/login')
    if not user.get('S_ID', None):
        flash('你沒有權限', 'danger')
        return redirect('/')

    user_id = user.get('S_ID', None)
    courses = get_student_enroll_course(user_id)
    return render_template('auth/student_course.html', courses=courses)

@auth_app.route('/user/mypayment')
def show_student_payment():
    user = session.get('user')
    if not user:
        flash('請先登入', 'danger')
        return redirect('/login')

    user_id = user.get('S_ID', None)
    u = get_student_enroll_payment(user_id)
    return render_template('auth/student_payment.html', user=u)

@auth_app.route('/user/enroll/<course_id>', methods=['GET'])
def enroll_course(course_id):
    user = session.get('user')
    if not user:
        flash('請先登入', 'danger')
        return redirect('/login')

    today = date.today()
    e_date = today.strftime("%Y-%m-%d")

    print(f'course id: {course_id}') # course id: 7
    print(f'user: {user}') # user: {'EMAIL': 'g23523@gmail.com', 'NAME': 'goodgood', 'S_ID': 4}
    print(f'e_date: {e_date}') # e_date: 2022-04-20

    enrollment = {
        "course_id": course_id,
        "s_id": user['S_ID'],
        "e_date": e_date
    }
    
    is_success = insert_to_enroll(enrollment)

    if is_success:
        flash("註冊課程成功", "success")

        course_info = get_one_course(course_id)
        print(f'course info: {course_info}')

        msg_title = f"歡迎註冊 {course_info['TITLE']}"
        print(f'email title: {msg_title}')
        msg_sender = ('DB 期中 Group 13', 'testcodepython1126@gmail.com')
        msg_receiver = [user['EMAIL']] # TODO: to variable
        msg_content = f"歡迎註冊 {course_info['TITLE']}, 期待您能從這門課收穫到滿滿的知識!"

        with current_app.app_context():
            print('send')
            send_mail(
                msg_title, msg_sender, msg_receiver, msg_content,
                name=user['NAME'],
            )
        return redirect(f'/classroom/{course_id}')

    else:
        flash("你已經註冊過該課程", "info")
        return redirect(f'/courses/{course_id}')

    
