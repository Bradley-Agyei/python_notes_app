# File is used to set up routes to different pages on app

from flask import Blueprint #Blueprint is used to organize the different views. Views can be defined in multiple files.

views = Blueprint('views', __name__)

#Define a view blueprint to route user to home page when '/' is used. 
@views.route('/')
def home():
    return "<h1>Test</h1>"