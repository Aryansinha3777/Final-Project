#importing necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
#creating an instance of SQLAlchemy and assigning it to variable db
db = SQLAlchemy()
#defining a create_app function to initialize and configure the flask application
def create_app():
    app=Flask(__name__)
    #configure the flask application using config class from config module
    app.config.from_object(config)
    #initializing the database
    db.init_app(app)
    #register the imported blueprint with flask application
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)
    #return the flask app instance from create_app function
    return app