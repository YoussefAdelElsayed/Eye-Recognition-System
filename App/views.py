from flask import render_template, redirect, url_for, session, request, g, flash, Response
from app import app, db
from app import models
from app import iris_recognition
import requests
import os

@app.before_request
def before_request():
    g.user = None
    users = models.Admin.query.all()
    if 'username' in session:
        for user in users:
            if user.username == session['username']:
                g.user = user
                
@app.route('/')
def home():
    return render_template('home.html')                

@app.route('/attend', methods=['GET', 'POST'])
def attend():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No image was uploaded')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        name = iris_recognition.testIris(path)
        os.remove(path)
        
        user = models.user.query.filter(name == name).first()
        if not user:
            flash("We couldn't identify you! Please try again.")
        else:
            if name == 'unmatch':
                flash("We couldn't identify you! Please try again.")
            else:
                attendance = models.attendance(userID=user.id)
                db.session.add(attendance)
                db.session.commit()
                name = name.split('/')[1]
                flash(f"Welcome, {name}!")
        return redirect(request.url)
        
    return render_template('attendance.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        phone = request.form['phone']
        age = request.form['age']
        file = request.files['file']
        
        user = models.user(id=id, name=name, email=email, address=address, gender=gender, phoneNumber=phone, age=age)
        db.session.add(user)
        db.session.commit()
        
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        try:
            os.makedirs(path)
        except:
            flash('User already exists')
            return redirect('/')
        path = os.path.join(path, file.filename)
        file.save(path)
        iris_recognition.trainModel()
        flash('Successfully Added.')
        return redirect('/')
        
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')
