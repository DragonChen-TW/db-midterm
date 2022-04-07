from flask import Blueprint, render_template
from backend.users import get_all_users

front_app = Blueprint('front_app', __name__)

@front_app.route('/')
def show_all_users():
    users = get_all_users()
    return render_template('home/users.html', users=users)