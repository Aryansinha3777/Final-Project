#import the os module to work with file paths and environment variable
import os
#get the absolute path of directory containing the current file to determine the base directory
basedir=os.path.abspath(os.path.dirname(__file__))
#creating a class named config to hold setting for flask application
class Config:
    #define the secret key attribute to be used for cryptographic operation
    SECRET_KEY = os.environ.get('a_secret_key')
    #defining a sqlalchemy_database_uri attribute to specify the database connection url 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
    #defining aa sqlalchemy_track_modification attribute to disable modification tracking for sqlalchemy
    SQLALCHEMY_TRACK_MODIFICATIONS=False