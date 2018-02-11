import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import psycopg2
from tools import *

app = Flask(__name__)
app.debug = True

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/circus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
import models


@app.template_global()
def static_include(filename):
    fullpath = os.path.join(app.static_folder, filename)
    with open(fullpath, 'r') as f:
        return f.read()

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/admin/shift')
def createShift():
	return render_template('addShift.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/employees')
def getEmployees():
    employees = db.session.query(models.User).all()
    response = []
    for val in employees:
        emp = val.__dict__
        response.append({
            'id': emp['employee_id'],
            'first_name': emp['first_name'],
            'last_name': emp['last_name'],
            'email': emp['email_address']
            })
    return json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/employees/<employee_id>')
def getEmployee(employee_id):
    employee = db.session.query(models.User).get(employee_id)
    emp_dict = employee.__dict__
    response = {
        'id': employee_id,
        'first_name': emp_dict['first_name'],
        'last_name': emp_dict['last_name'],
        'email': emp_dict['email_address']
    }
    return json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))



@app.route('/employees/shift/<employee_id>')
def getEmployeeShifts(employee_id):
	shifts = []
	employee = db.session.query(models.Shift).filter(models.Shift.employee_id == employee_id).all()
	for emp in employee:
		emp_dict = emp.__dict__
		response = {
	    	'shift_id': emp_dict['shift_id'],
			'employee_id': emp_dict['employee_id'],
			'date': emp_dict['date'],
			'start_time': emp_dict['start_time'],
			'end_time': emp_dict['end_time'],
			'location': emp_dict['location'],
			'category_id': emp_dict['category_id'],
			'complete': emp_dict['complete']
	    }
		shifts.append(response)	
	return json.dumps(shifts, sort_keys=True, indent=4, separators=(',', ': '), default = date_convert)

@app.route('/dashboard')
def getDashboard():
    return 'Not yet.'

@app.route('/dbtest')
def getDBStuff():
    return 'oops'
if __name__ == '__main__':
    app.run()