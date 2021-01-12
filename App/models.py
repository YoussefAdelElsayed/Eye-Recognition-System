


class user(db.Model):
    name = db.Column(db.string(100))
    email = db.Column(db.string(100))
    address = db.Column(db.string(100))
    phoneNumber = db.Column(db.string(13))
    gender = db.Column(db.string(6))
    nationalID = db.Column(db.string(14), primary_key=True)
    age = db.column(db.integer)
    eyeID = db.column(db.integer)

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)
    
    
    
class Admin(db.Model):
    adminID = db.column(db.integer, primary_key=True)
    password = db.column(db.string(20))

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)
    
    
    
class attendance(db.Model):
    attendanceID = db.column(db.integer, primary_key=True)
    Department = db.column(db.string(30))

def __init__(self, *args, **kwargs):
    super().__int__(*args, **keargs)