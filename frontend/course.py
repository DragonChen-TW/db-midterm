from flask import Blueprint, render_template
from backend.courses import get_all_courses, get_one_courses, get_courses_by_instructor


course_app = Blueprint('course_app', __name__)

@course_app.route('/courses')
def show_all_courses():
    courses = get_all_courses()
    return render_template('course/course_list.html', courses=courses)

@course_app.route('/courses/<course_id>')
def show_one_course(course_id):
    course = get_one_courses(course_id)
    return render_template('course/course_detail.html', course=course)

# Course by instructor
@course_app.route('/instructor_home/<instructor_id>')
def show_instructor_home(instructor_id):
    print(instructor_id)
    courses_by_instructor = get_courses_by_instructor(instructor_id)
    return render_template('course/course_by_instructor.html', 
    instructor_id=instructor_id, courses=courses_by_instructor)