# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for
import pymongo

# -- Initialization section --
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
# name of database
app.config['MONGO_DBNAME'] = 'goals'
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:85Uyd3llgvemqMeo@cluster0.mkhj9.mongodb.net/goals?retryWrites=true&w=majority'
mongo = PyMongo(app)
# -- Routes section --


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')


@app.route('/save', methods=['GET', 'POST'])
def save():
    collection = mongo.db.login
    connect_user = list(collection.find({'name': session['username']}))
    scratchpad = connect_user[0]['scratchpad']
    query = {'name': session['username']}
    if request.method == 'POST':
        note = request.form['note']
        newNote = { "$set": { "scratchpad": note } }
        collection.update_one(query, newNote)
        return render_template('smart.html', note=scratchpad)
    return render_template('smart.html', note=scratchpad)




@app.route('/smart', methods=['GET', 'POST'])
def smarty():
    collection = mongo.db.login
    connect_user = list(collection.find({'name': session['username']}))
    current_goal = connect_user[0]['current-goals']
    query = {'name': session['username']}
    if request.method == 'POST':
        new_goal = request.form['new_goal']
        current_goal.append(new_goal)
        newvalues = { "$set": { "current-goals": current_goal  } }
        collection.update_one(query, newvalues)
        return render_template('smart.html', current=current_goal)
    return render_template('smart.html', current=current_goal)

@app.route('/complete', methods=['GET', 'POST'])
def complete(): 
    collection = mongo.db.login
    connect_user = list(collection.find({'name': session['username']}))
    current_goal = connect_user[0]['current-goals']
    complete_goal = connect_user[0]['completed-goals']
    query = {'name': session['username']}
    if request.method == 'GET': 
        return render_template('smart.html', complete=complete_goal)
    if request.method == 'POST':
        checked_goals = list(request.form) 
        for checked in checked_goals: 
            for goal in current_goal: 
                if goal == checked: 
                    complete_goal.append(goal)
                    newComplete = { "$set": { "completed-goals": complete_goal } }
                    collection.update_one(query, newComplete)
                    current_goal.remove(goal)
                    newDelete = { "$set": { "current-goals": current_goal } }
                    collection.update_one(query, newDelete)
                    return render_template('smart.html', complete=complete_goal)
    return render_template('smart.html', complete=complete_goal)
                    
                    
                    
    #                 return redirect(url_for('smarty'), complete=complete_goal)
    # return redirect(url_for('smarty'), complete=complete_goal)
    

@app.route('/signlog', methods=['GET', 'POST'])
def signlog():
    # are they posting with form
    if request.method == 'POST':
        # connect to database
        login = mongo.db.login
        # do something with database-does anyone have this name?
        existing_user = login.find_one({'name': request.form['username']})
        # does user not exists? add to database then
        if existing_user is None:
            # add user to the database
            login.insert(
                {'name': request.form['username'], 'password': request.form['password'], 'current-goals': [], 'scratchpad': "", 'completed-goals': []})
            # make session for the user
            session['username'] = request.form['username']
            return redirect(url_for('profile'))
        return 'The username already exists'
    return render_template('signlog.html')
# login to account
@app.route('/log', methods=['GET', "POST"])
def login():
    if request.method == 'GET': 
        return render_template('/log.html')
    if request.method == 'POST': 
        # connect to database
        login = mongo.db.login
        # get login for users
        login_user = login.find_one({'name': request.form['username']})
            # check password matches
        if login_user:
            # check does the password they put in match password in database
            if request.form['password'] == login_user['password']:
                # start a session
                session['username'] = request.form['username']
                return redirect(url_for('profile'))
        # password or username incorrect?
        return 'Invalid username/password combination'
# LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/timeline.html')
def timeline():
    return render_template('timeline.html')


@app.route('/retirement', methods=['POST', 'GET'])
def retirement(): 
    if request.method == 'GET': 
        return render_template('timeline.html')
    if request.method == 'POST': 
        pmt = int(request.form['pmt'])
        i = int(request.form['i'])
        fv = int(request.form['fv'])
        beg_age = int(request.form['beg_age'])
        a = 0
        n = 0
        while (a < fv):
            n += 1
            a += pmt * (1. + i/100.)**n
        retir_age = beg_age + n
        return render_template('timeline.html', retir_age=retir_age)
    

@app.route("/calculator", methods=['POST','GET'])
def calculator():
  z= ''
  if request.method=='POST' and 'p' in request.form and 'n' in request.form and 'r' in request.form and 'y' in request.form:
    p = float(request.form.get('p'))
    n = float(request.form.get('n'))
    r = float(request.form.get('r'))
    y = float(request.form.get('y'))
    fv = p * (((1 + ((r/100.0)/n)) ** (n*y)))
    z = round(fv,2)  
  return render_template('timeline.html', z=z)




