from flask import (Blueprint, render_template, flash, redirect)
from backend.courses import get_courses_by_instructor, get_all_courses, remove_one_course


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

@instru_app.route('/instructor/<course_id>/delete', methods=['POST'])
def delete_one_course(course_id):
    print('delete')
    course_id = int(course_id)

    instructor_id = 1
    # instructor_id = session.user.get('i_id', None)

    courses = get_courses_by_instructor(instructor_id)
    c_ids = [c['COURSE_ID'] for c in courses]

    if course_id not in c_ids:
        flash('沒有權限刪除此課程', 'danger')
        print('no permission')
    else:
        remove_one_course(course_id)
        flash(f'刪除課程 {course_id} 成功', 'success')
        print('success')

    return redirect('/instructor_home/')

@instru_app.route('/instructor/create', methods=['POST'])
def assign_new_course_id():
    print('Create new course')

    course_amount = len(get_all_courses())

    new_course_id = int(course_amount) + 1
    print(new_course_id)

    # get instructor id from session !!
    instructor_id = 1
    # instructor_id = session.user.get('i_id', None)

    return render_template('instructor/create_new_course.html', course = new_course_id)

@instru_app.route('/courses/submit_new_course', methods=['POST'])
def insert_new_course():
    print(f'insert new course')
    


# # Instructor edit course
# @instru_app.route('/instructor_home/editCourse')
# def show_instructor_home(course_id):
#     print(course_id)
#     # courses_by_instructor = get_courses_by_instructor(instructor_id)
#     return render_template('course/edit_course.html', course=course_id)