from flask import Flask, Blueprint
from frontend.course import course_app
from frontend.auth import auth_app
from frontend.instructor import instru_app

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

if __name__ == '__main__':
    app.run(port=8765, debug=True)