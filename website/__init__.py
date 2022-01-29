#Makes 'website' folder a python package. Allows us to later import folder and run what is inside __init__. 

from flask import Flask

# Function to initialize flask app, __name__ is the name of the file that is being run. 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'welcometoflaskframework'  # Secures cookies/session data
    return app

