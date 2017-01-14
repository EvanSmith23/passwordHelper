#!flask/bin/python
from flask import Flask, Blueprint, request, render_template
from extensions import connect_to_database

db = connect_to_database()

# app = Flask(__name__)
createUser = Blueprint('createUser', __name__, template_folder='htmlFiles')

@createUser.route('/user/', methods = ['GET','POST'])
def index():
	if request.method == 'GET':    
		options = {
			"firstname" : "First Name",
			"lastname" : "Last Name"
		}
		return render_template("createUser.html", **options)

	elif request.method == 'POST':
	   	firstname = request.form['firstname']
	   	lastname = request.form['lastname']
	   	question1 = request.form['question1']
	   	answer1 = request.form['answer1']
	   	question2 = request.form['question2']
	   	answer2 = request.form['answer2']
	   	question3 = request.form['question3']
	   	answer3 = request.form['answer3']

		query = 'UPDATE users SET firstname=%s, lastname=%s, question1=%s, answer1=%s, question2=%s, answer2=%s, question3=%s, answer3=%s WHERE firstname=%s'
		cur = db.cursor()
		cur.execute(query, (firstname,lastname,question1,answer1,question2,answer2,question3,answer3,firstname, ) )
		result = cur.fetchall()

		options = {
			"firstname" : firstname,
			"lastname" : lastname,
			"question1" : question1,
			"answer1" : answer1,
			"question2" : question2,
			"answer2" : answer2,
			"question3" : question3,
			"answer3" : answer3
		}
		return render_template("createUser.html", **options)
 