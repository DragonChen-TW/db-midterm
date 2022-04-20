from flask import (
    Blueprint, render_template,
    request, session,
    redirect, url_for, send_file,
    flash,
)
from backend.courses import (
    get_one_course, get_course_contents, get_student_course_contents,
    get_one_content,
)
from backend.student import (
    insert_to_studentcontent,
    update_to_studentcontent,
)

classroom_app = Blueprint('classroom_app', __name__)

@classroom_app.route('/classroom/<course_id>')
def show_all_courses(course_id):
    c_id = int(course_id)

    # show course details
    course_desc = get_one_course(c_id)
    
    # list all chaptet/contents
    contents = get_student_course_contents(c_id)
    return render_template('classroom/view_course.html', course_desc=course_desc, contents=contents)

@classroom_app.route('/classroom/content/<content_id>/view')
def show_file_content(content_id):
    student = session.get('user')
    content = get_one_content(content_id)

    student_content = {
        's_id': student['S_ID'],
        'content_id': content_id,
        'status': 'not yet'
    }
    insert_to_studentcontent(student_content)

    return send_file(content['FILE_PATH'])


@classroom_app.route('/classroom/content/<content_id>/complete')
def complete_content(content_id):
    student = session.get('user')
    # content = get_one_content(content_id)

    student_content = {
        's_id': student['S_ID'],
        'content_id': content_id,
    }
    ok = update_to_studentcontent(student_content)

    course_id = request.values.get('COURSE_ID')
    if ok and course_id:
        return redirect(f'/classroom/{course_id}')
    elif not ok:
        flash('完成課程失敗', 'danger')
        return redirect('/user/mycourse')
    else:
        flash('找無原始課程路徑', 'danger')
        return redirect('/user/mycourse')