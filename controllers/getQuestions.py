#!flask/bin/python
from flask import Flask, Blueprint, request, render_template

# app = Flask(__name__)
getQuestions = Blueprint('getQuestions', __name__, template_folder='htmlFiles')

@getQuestions.route('/', methods = ['GET','POST'])
def index():
  if request.method == 'GET':
    options = {
      "firstname" : "First Name",
      "lastname" : "Last Name"
    }
    return render_template("getQuestions.html", **options)
  
  elif request.method == 'POST':
    
    firstname=request.form['firstname']
    lastname=request.form['lastname']
    options = {
      "firstname" : firstname,
      "lastname" : lastname
    }
    return render_template("getQuestions.html", **options)
