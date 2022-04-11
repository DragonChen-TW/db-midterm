from flask import Blueprint, render_template
from backend.users import get_all_users


auth_app = Blueprint('auth_app', __name__)

@auth_app.route('/')
def show_all_users():
    users = get_all_users()
    return render_template('home/users.html', users=users)