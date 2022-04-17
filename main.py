from flask import Flask, Blueprint
from frontend.course import course_app
from frontend.auth import auth_app

app = Flask(__name__)

app.secret_key = 'DB-midterm, HI'

app.register_blueprint(course_app)
app.register_blueprint(auth_app)

if __name__ == '__main__':
    app.run(port=8765, debug=True)