#Makes 'website' folder a python package. Allows us to later import folder and run what is inside __init__. 

from flask import Flask

# Function to initialize flask app, __name__ is the name of the file that is being run. 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'welcometoflaskframework'  # Secures cookies/session data

    # Registering blueprints. First, import, shown directly below. Second, register blueprints.  
    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

