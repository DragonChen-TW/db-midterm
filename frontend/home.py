from flask import Blueprint, render_template
from backend.users import get_all_users
from backend.courses import get_all_courses


front_app = Blueprint('front_app', __name__)

@front_app.route('/')
def show_all_users():
    users = get_all_users()
    return render_template('home/users.html', users=users)


@front_app.route('/courses')
def show_all_courses():
    courses = get_all_courses()
    return render_template('home/course_list.html', courses=courses)