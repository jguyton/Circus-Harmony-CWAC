from app import *
from datetime import datetime

# users class
class User(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(20))
    email_address = db.Column(db.String(120), unique=True)
    
    def __init__(
        self,
        first_name,
        last_name,
        phone_number,
        email_address
    ):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address

    def __repr__(self):
        return '{first_name:%s, last_name: %s, phone_number: %s, email_address: %s }'%(self.first_name, self.last_name, self.phone_number, self.email_address)

# shift class
class Shift(db.Model):
    shift_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    location = db.Column(db.String(120))
    category_id = db.Column(db.Integer)
    complete = db.Column(db.Boolean)

    def __init__(
        self,
        employee_id,
        date,
        start_time,
        end_time,
        location,
        category_id,
        complete
    ):

        self.employee_id = employee_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.category_id = category_id
        self.complete = complete

    def __repr__(self):
        return '{shift_id:%s, employee_id: %s, date: %s, start_time: %s, end_time: %s, location: %s, category_id: %s, complete: %s }'%(self.shift_id, self.employee_id, self.date, self.start_time, self.end_time, self.location, self.category_id, self.complete)

# job class
class Job(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    
    def __init__(
        self,
        name,
    ):

        self.name = name

    def __repr__(self):
        return '{name:%s, category_id: %s, location_id: %s}'%(self.name, self.category_id, self.location_id)


# location class
class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))

    def __init__(
        self,
        name,
    ):
        self.name = name

    def __repr__(self):
        return '{name:%s, address: %s}'%(self.name, self.address)


# category class
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(250))
    location = db.Column(db.String(250))
    name = db.Column(db.String(250))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)


    def __init__(
        self,
        name, 
        job,
        location,
        start_time,
        end_time
    ):
        self.name = name
        self.job = job
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{name:%s}'%(self.name)

