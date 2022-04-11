from flask import Blueprint, render_template
from backend.users import get_all_students

auth_app = Blueprint('auth_app', __name__)

@auth_app.route('/')
def show_all_students():
    students = get_all_students()
    print('stu', students)
    return render_template('auth/user_list.html', students=students)