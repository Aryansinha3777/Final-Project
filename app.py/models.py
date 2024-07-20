#importing the db instance from current module
from . import db
#create a class named employee that inherit from db.module
class Employee(db.Model):
    #define the columns of employee table using db.column
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    position = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128),nullable=False)
#creating the method to_dict to convert the employee instance to dictionary format
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "department": self.department
        }      