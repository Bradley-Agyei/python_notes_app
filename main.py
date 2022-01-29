from distutils.log import debug
from website import create_app

app = create_app()

# If the name of the file that is running is 'main', the run the flask app. 
if __name__ == '__main__':
    app.run(debug=True)     #runs flask app, debug=True allows for automatic updates on app when code is updated. 