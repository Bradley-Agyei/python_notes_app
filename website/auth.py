from flask import Blueprint #Blueprint is used to organize the different views. Views can be defined in multiple files.

auth = Blueprint('auth', __name__)

#Route users to login page
@auth.route('/login')
def login():
    return "<p>Login</p>"


#Route users to logout page
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


#Route users to signup page
@auth.route('/signup')
def sign_up():
    return "<p>Sign Up</p>"
