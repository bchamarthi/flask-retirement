# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for
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
@app.route('/timeline.html')
def timeline():
    return render_template('timeline.html')
@app.route('/info.html')
def info():
    return render_template('info.html')
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
@app.route('/signlog.html', methods = ['GET', 'POST'])
def signlog():
    return render_template('signlog.html')
# @app.route('/profile.html')
# def profile():

# @app.route('', methods = ['GET', 'POST'])
# def smartgoal():
#     if request.method == 'POST':
#         new_goal = request.form['new_goal']
#         print(new_goal)
    

@app.route('/about.html')
def abouty():
    collection = mongo.db.goals
    current = collection.find({})
    # music = list(collection.find({}).sort('title', 1))
    # music = list(collection.find({}).sort('artist', 1).limit(3))
    return render_template('about.html', current = current)



@app.route('/smart', methods = ['GET', 'POST'])
def smarty():
    if request.method == 'POST': 
        new_goal = request.form['new_goal']
        current = mongo.db.current
        current.insert({'goal': new_goal})
        return redirect('smart.html')
    else: 
        return redirect('smart.html')