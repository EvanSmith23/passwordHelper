import MySQLdb
import os

def connect_to_database():
	
	#create arguments to connect to database
	options = {
		'host' : '0.0.0.0',
		'user' : 'root',
		'passwd' : 'root',
		'db' : 'pH',
	}

	#create a connection object
	db = MySQLdb.connect(**options)
	db.autocommit(True)

	#return connection object
	return db
