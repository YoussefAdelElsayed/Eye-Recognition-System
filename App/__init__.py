from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
app.config['UPLOAD_FOLDER'] = 'Input_database'

db = SQLAlchemy(app)
api = Api(app)
admin = Admin(app)

from app import models
from app import views

admin.add_view(ModelView(models.user, db.session))
admin.add_view(ModelView(models.attendance, db.session))
