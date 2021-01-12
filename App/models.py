from app import db
from datetime import date

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phoneNumber = db.Column(db.String(13))
    gender = db.Column(db.String(6))
    age = db.Column(db.Integer)

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)
    
    
# might be omitted
class Admin(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)
    
    
class attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today())
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)
    