from flask import Blueprint, render_template
from backend.courses import get_courses_by_instructor


instru_app = Blueprint('instru_app', __name__)

# Course by instructor
@instru_app.route('/instructor_home/')
def show_instructor_home():
    instructor_id = 1
    # instructor_id = session.user.get('i_id', None)

    print(instructor_id)
    courses_by_instructor = get_courses_by_instructor(instructor_id)
    return render_template(
        'instructor/course_by_instructor.html', 
        instructor_id=instructor_id, courses=courses_by_instructor
    )

# # Instructor edit course
# @instru_app.route('/instructor_home/editCourse')
# def show_instructor_home(course_id):
#     print(course_id)
#     # courses_by_instructor = get_courses_by_instructor(instructor_id)
#     return render_template('course/edit_course.html', course=course_id)