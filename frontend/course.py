from flask import (
    Blueprint, render_template,
    request,
    redirect, url_for,
    flash,
)
from backend.courses import (
    get_all_courses, get_one_course, get_courses_by_instructor,
    remove_one_course,
)

course_app = Blueprint('course_app', __name__)

@course_app.route('/courses')
def show_all_courses():
    courses = get_all_courses()
    return render_template('course/course_list.html', courses=courses)

@course_app.route('/courses/<course_id>', methods=['GET'])
def show_one_course(course_id):
    course = get_one_course(course_id)
    return render_template('course/course_detail.html', course=course)

# @course_app.route('/courses/<course_id>', methods=['POST'])
# def edit_one_course(course_id):
#     course = get_one_course(course_id)
#     return render_template('course/course_detail.html', course=course)

@course_app.route('/courses/<course_id>/delete', methods=['POST'])
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