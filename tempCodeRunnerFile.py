from flask import Flask, Blueprint
from frontend.course import course_app
from frontend.auth import auth_app
from frontend.instructor import instru_app

app = Flask(__name__)

