#!flask/bin/python
from flask import Flask, Blueprint, request, render_template

# app = Flask(__name__)
createUser = Blueprint('createUser', __name__, template_folder='htmlFiles')

@createUser.route('/user/', methods = ['GET'])
def index():
  if request.method == 'GET':
    options = {
      "firstname" : "First Name",
      "lastname" : "Last Name"
    }
    return render_template("createUser.html", **options)
