from flask import Flask, Blueprint, render_template, send_from_directory
from frontend.course import course_app
from frontend.auth import auth_app
from frontend.instructor import instru_app
from frontend.classroom import classroom_app

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'db.midterm.automation135@gmail.com'
app.config['MAIL_PASSWORD'] = 'bdxyccydjmbaivos'
# Original password 'automation135'
# Phone +358414869841
# Phone website https://receive-sms-free.cc/Free-Finland-Phone-Number/358414869841/

app.secret_key = 'DB-midterm, HI'

app.register_blueprint(course_app)
app.register_blueprint(auth_app)
app.register_blueprint(instru_app)
app.register_blueprint(classroom_app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# @app.route('/manifest.json') # for PWA
# def manifest():
#     return app.send_from_directory('static', 'manifest.json')

if __name__ == '__main__':
    app.run(port=8765, debug=True)