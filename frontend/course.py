from flask import (
    Blueprint, render_template,
    request,
    redirect, url_for,
    flash,
)
from backend.courses import (
    get_all_courses, get_one_course, get_courses_by_instructor,
    remove_one_course, get_all_courses_search
)
from backend.feedback import (
    get_all_feedbacks,
    get_my_feedback,
)

course_app = Blueprint('course_app', __name__)

@course_app.route('/courses', methods=['GET', 'POST'])
def show_all_courses():

    if request.method == 'POST':
        course_content = {}
        
        if request.values.get('course_title'):
            course_content["c_title"] = request.values.get('course_title')
        if request.values.get('course_cate'):
            course_content["c_cate"] = request.values.get('course_cate')
        if request.values.get('course_lang'):
            course_content["c_lang"] = request.values.get('course_lang')
        
        print('coutse_content', course_content)
        
        if len(course_content) == 0:
            courses = get_all_courses()
        else:
            courses = get_all_courses_search(course_content)
    else:
        courses = get_all_courses()

    return render_template('course/course_list.html', courses=courses)

# @course_app.route('/courses/search', methods=['GET', 'POST'])
# def show_all_courses_search():

#     if request.method == 'POST':
#         print(f'[message]  insert new course.')
#         course_content = {
#             "c_title": request.values.get('course_title')
#         }
#         courses = get_all_courses_search(course_content)

#     return render_template('course/course_list.html', courses=courses)

@course_app.route('/courses/<course_id>', methods=['GET'])
def show_one_course(course_id):
    course = get_one_course(course_id)
    my_feedback = get_my_feedback(course_id)
    print('my_fb', my_feedback)
    feedbacks = get_all_feedbacks(course_id)
    print('fffeedbacks', feedbacks)
    return render_template('course/course_detail.html',
        course=course,
        my_feedback=my_feedback, feedbacks=feedbacks
    )

# @course_app.route('/courses/<course_id>', methods=['POST'])
# def edit_one_course(course_id):
#     course = get_one_course(course_id)
#     return render_template('course/course_detail.html', course=course)

# @course_app.route('/instructor/<course_id>/delete', methods=['POST'])
# def delete_one_course(course_id):
#     print('delete')
#     course_id = int(course_id)

#     instructor_id = 1
#     # instructor_id = session.user.get('i_id', None)

#     courses = get_courses_by_instructor(instructor_id)
#     c_ids = [c['COURSE_ID'] for c in courses]

#     if course_id not in c_ids:
#         flash('沒有權限刪除此課程', 'danger')
#         print('no permission')
#     else:
#         remove_one_course(course_id)
#         flash(f'刪除課程 {course_id} 成功', 'success')
#         print('success')

#     return redirect('/instructor_home/')

# @course_app.route('/instructor/create', methods=['POST'])
# def delete_one_course():
#     print('Create new course')

#     course_amount = len(get_all_courses())

#     new_course_id = int(course_amount) + 1
#     print(new_course_id)

#     # get instructor id from session !!
#     instructor_id = 1
#     # instructor_id = session.user.get('i_id', None)

#     return redirect('instructor/create_new_course.html', course = new_course_id, instructor = instructor_id)