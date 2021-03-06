#!flask/bin/python
from flask import Flask, Blueprint, request, render_template
from extensions import connect_to_database
import MySQLdb

# app = Flask(__name__)
getQuestions = Blueprint('getQuestions', __name__, template_folder='templates')

db = connect_to_database()

@getQuestions.route('/', methods = ['GET','POST'])
def index():
  if request.method == 'GET':
    options = {
      "firstname" : "",
      "lastname" : ""
    }
    return render_template("getQuestions.html", **options)

  elif request.method == 'POST':
    firstname=request.form['firstname']

    query = 'SELECT * FROM users WHERE firstname=%s'
    cur = db.cursor()
    cur.execute(query, (firstname) )
    result = cur.fetchall()

    firstname = result[0]['firstname']
    lastname = result[0]['lastname']
    website = result[0]['lastname']
    question1 = result[0]['question1']
    answer1 = result[0]['answer1']
    question2 = result[0]['question2']
    answer2 = result[0]['answer2']
    question3 = result[0]['question3']
    answer3 = result[0]['answer3']

    options = {
      "firstname" : firstname,
      "lastname" : lastname,
      "website" : website,
      "question1" : question1,
      "answer1" : answer1,
      "question2" : question2,
      "answer2" : answer2,
      "question3" : question3,
      "answer3" : answer3
    }
    return render_template("getQuestions.html", **options)
