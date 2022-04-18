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

# Can call `flash(msg_text, alert_type)` to show a temporary message on page
# alert_type could be 'success', 'danger', 'info', etc.
# View https://getbootstrap.com/docs/5.1/components/alerts/#link-color to get all the types

auth_app = Blueprint('auth_app', __name__)

@auth_app.route('/')
def show_snaps():
    num_student, num_insturctor, num_course, num_category, num_popular = get_all_snaps()
    print(num_student, num_insturctor, num_course, num_category, num_popular)
    return render_template('home/user_list.html', num_student=num_student, num_insturctor=num_insturctor, 
    num_course=num_course, num_category=num_category, num_popular=num_popular)

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
            msg_receiver = ['teacher144123@gmail.com'] # TODO: to variable
            msg_content = f''

            with current_app.app_context():
                print('send')
                send_mail(
                    msg_title, msg_sender, msg_receiver, msg_content,
                    confirm_url=f'{request.url_root}?value={value}',
                    name=name,
                )
            
            flash('註冊成功，請至信箱完成驗證', 'success')
            return redirect('/login')
    
    return render_template('auth/sign_up.html')

@auth_app.route('/confirm', methods=['GET'])
def confirm_registraion():
    value = request.values.get('value')

    # TODO


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
    u = get_student_enroll_course(user_id)
    return render_template('auth/student_course.html', user=u)

@auth_app.route('/user/mypayment')
def show_student_payment():
    user = session.get('user')
    if not user:
        flash('請先登入', 'danger')
        return redirect('/login')

    user_id = user.get('S_ID', None)
    u = get_student_enroll_payment(user_id)
    return render_template('auth/student_payment.html', user=u)