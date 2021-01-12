

@app.before_request
def before_request():
    g.user = None
    users = models.Admin.query.all()
    if 'username' in session:
        for user in users:
            if user.username == session['username']:
                g.user = user
                
@app.route('/attend')
def home():
    return render_template('attendance.html')

@app.route('/signup')
def home():
    return render_template('signup.html')

@app.route('/about')
def home():
    return render_template('about.html')
