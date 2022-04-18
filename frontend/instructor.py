from webbrowser import get
from flask import Blueprint, render_template, flash, redirect, request
from backend.courses import (
    get_all_courses, get_one_course, get_courses_by_instructor,
    remove_one_course, get_course_chapter, get_course_contents
    )
from backend.instructor import (
    get_instructor_detail,
    insert_to_course, insert_to_course_instructor,
)

instru_app = Blueprint('instru_app', __name__)

@instru_app.route('/instructor/<instructor_id>')
def show_instructor_profile(instructor_id):
    i = get_instructor_detail(instructor_id)
    return render_template('instructor/instructor_profile.html', user=i)

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

    return render_template('instructor/create_new_course.html', course=new_course_id)

@instru_app.route('/instructor/submit_new_course', methods=['POST'])
def insert_new_course():
    instructor_id = 1

    print(f'[message]  Insert new course.')
    course_content = {
        "c_id": request.values.get('course_id'),
        "c_title": request.values.get('course_title'),
        "c_cate": request.values.get('course_cate'),
        "c_brief": request.values.get('course_brief'),
        "c_fee": request.values.get('course_fee'),
        "c_lang": request.values.get('course_lang'),
    }
    insert_to_course(course_content)
    insert_to_course_instructor(request.values.get('course_id'), instructor_id)

    # after insertion, return to /instructor_home
    return redirect('/instructor_home/')


# # Instructor edit course
# @instru_app.route('/instructor_home/editCourse')
# def show_instructor_home(course_id):
#     print(course_id)
#     # courses_by_instructor = get_courses_by_instructor(instructor_id)
#     return render_template('course/edit_course.html', course=course_id)

@instru_app.route('/instructor/<course_id>/view', methods=['POST'])
def view_course_stats(course_id):
    print(f'course_id: {course_id}')
    c_id = int(course_id)

    # show course details
    course_desc = get_one_course(c_id)
    print(course_desc)
    
    # list all chaptet/contents
    contents = get_course_contents(c_id)

    for content in contents:
        print(content)
        
    # contents = []
    
    return render_template('/instructor/view_course_stats.html', course_desc=course_desc, contents=contents)