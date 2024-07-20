#importing blueprint,jsonify and request
from flask import Blueprint, jsonify,request
#importing Employee and db function from models module
from models import Employee,db
#creating an instance of blueprint with name-'main' and import name-(__name__)
main = Blueprint('main',__name__)
#defining a route for root url('/) that return a welcome message
@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Employee Management System!"})
#defining a route for /employee url that return a placeholder for employee list
#GET request to fetch all employee
@main.route('/employee', methods=['GET'])
def get_employees():
    #query all employee record from database
    employees = Employee.query.all()
    #converting each employee record to a dictionary
    return jsonify({"employee": [employee.to_dict() for employee in employees]})
#POST request to create a new employee
@main.route('/employee', methods=['POST'])
def create_employee():
    #parsing the incoming json data from request
    data=request.get_json()
    #create new employee object with provided data
    new_employee = Employee(
        name=data['name'],
        position=data['position'],
        department=data['department']
    )
    #adding new employee to database and commit the transaction
    db.session.add(new_employee)
    db.session.commit()
    #returning a success message in json format with a status code of 201
    return jsonify({"message": "Employee create successfully!"}),201
#PUT request to update an employee id
@main.route('/employee/<int:id>',methods=['PUT'])
def update_employee(id):
    #parsing the incoming json data from request
    data = request.get_json()
    #retrieving the employee record by id or return a 404 error
    employee= Employee.query.get_or_404(id)
    #updating the employee's attributes with provided data
    employee.name=data['name']
    employee.position= data['position']
    employee.department= data['department']
    #commit the change to database
    db.session.commit()
    #returning a success message in json format
    return jsonify({"message": "Employee updated successfully"})
#DELETE request to delete an employee id
@main.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    #retrieving the employee record by id or return 404 error
    employee = Employee.query.get_or_404(id)
    #deleting the employee record from database
    db.session.delete(employee)
    #commit the change to database
    db.session.commit()
    #returning a success message in json format
    return jsonify({"message": "Employee deleted successfully!"})