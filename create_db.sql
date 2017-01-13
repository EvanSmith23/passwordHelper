use testdb;

create table users (
	firstname varchar(40),
	lastname varchar(40),
	question1 varchar(40),
	answer1 varchar(40),
	question2 varchar(40),
	answer2 varchar(40),
	question3 varchar(40),
	answer3 varchar(40),
	PRIMARY KEY (firstname)
);