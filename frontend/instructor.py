from webbrowser import get
from flask import (
    Blueprint, render_template, flash, redirect, request, session
)
from backend.courses import (
    get_all_courses, get_one_course, get_courses_by_instructor,
    remove_one_course, get_course_chapter, get_course_contents
    )
from backend.instructor import (
    get_instructor_detail,
    insert_to_course, insert_to_course_instructor,
)

instru_app = Blueprint('instru_app', __name__)

def get_instructor_id():
    user = session.get('user')
    if not user:
        flash('請先登入', 'danger')
        return redirect('/login')
    if not user.get('I_ID', None):
        flash('你沒有權限', 'danger')
        return redirect('/')
    return user.get('I_ID')
        

@instru_app.route('/instructor/<instructor_id>')
def show_instructor_profile(instructor_id):
    i = get_instructor_detail(instructor_id)
    return render_template('instructor/instructor_profile.html', user=i)

# Course by instructor
@instru_app.route('/instructor_home/')
def show_instructor_home():
    instructor_id = get_instructor_id()
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

    instructor_id = get_instructor_id()
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

@instru_app.route('/instructor/create', methods=['GET', 'POST'])
def assign_new_course_id():
    instructor_id = get_instructor_id()

    if request.method == 'POST':
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

    print('Create new course')
    courses = get_all_courses()
    print('raw', courses)
    max_id = max([int(c['COURSE_ID']) for c in courses if c['COURSE_ID']])
    new_course_id = max_id + 1
    # print(new_course_id)

    return render_template('instructor/create_new_course.html', course=new_course_id)


# # Instructor edit course
# @instru_app.route('/instructor_home/editCourse')
# def show_instructor_home(course_id):
#     print(course_id)
#     # courses_by_instructor = get_courses_by_instructor(instructor_id)
#     return render_template('course/edit_course.html', course=course_id)

@instru_app.route('/instructor/<course_id>/view', methods=['GET'])
def view_course_stats(course_id):
    print(f'course_id: {course_id}')
    c_id = int(course_id)

    # show course details
    course_desc = get_one_course(c_id)
    print(course_desc)
    
    # list all chaptet/contents
    contents = get_course_contents(c_id)
    
    return render_template('/instructor/view_course_stats.html', course_desc=course_desc, contents=contents)