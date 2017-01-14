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
			"lastname" : "Last Name",
			"question1" : "question1",
			"answer1" : "answer1",
			"question2" : "question2",
			"answer2" : "answer2",
			"question3" : "question3",
			"answer3" : "answer3"

		}
		return render_template("createUser.html", **options)

	elif request.method == 'POST':
		
	   	firstname1 = request.form['firstname']
	   	lastname1 = request.form['lastname']
	   	website1 = request.form['website']
	   	question_1 = request.form['question1']
	   	answer_1 = request.form['answer1']
	   	question_2 = request.form['question2']
	   	answer_2 = request.form['answer2']
	   	question_3 = request.form['question3']
	   	answer_3 = request.form['answer3']

	   	# query is wrong, nothing in database, maybe syntax or maybe not connecting to database, try simpler checks to see fi connected to db

		query = 'INSERT INTO users (firstname,lastname,website,question1,answer1,question2,answer2,question3,answer3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		cur = db.cursor()
		cur.execute(query, (firstname1,lastname1,website1,question_1,answer_1,question_2,answer_2,question_3,answer_3) )
		result = cur.fetchall()

		# Do I need to fetch if I'm just updating

		options = {
			"firstname" : firstname1,
			"lastname" : lastname1,
			"website" : website1,
			"question1" : question_1,
			"answer1" : answer_1,
			"question2" : question_2,
			"answer2" : answer_2,
			"question3" : question_3,
			"answer3" : answer_3
		}
		return render_template("createUser.html", **options)
 