from flask import Blueprint, render_template #Blueprint is used to organize the different views. Views can be defined in multiple files.

auth = Blueprint('auth', __name__)

#Route users to login page
@auth.route('/login')
def login():
    return render_template("login.html")


#Route users to logout page
@auth.route('/logout')
def logout():
    return render_template("home.html")


#Route users to signup page
@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")
