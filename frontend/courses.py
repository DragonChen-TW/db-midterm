from flask import Blueprint, render_template
from backend.courses import get_all_courses, get_one_courses


course_app = Blueprint('course_app', __name__)

@course_app.route('/courses')
def show_all_courses():
    courses = get_all_courses()
    return render_template('home/course_list.html', courses=courses)

@course_app.route('/courses/<course_id>')
def show_one_course(course_id):
    course = get_one_courses(course_id)
    return render_template('home/course_detail.html', course=course)