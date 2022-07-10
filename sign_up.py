import re
from hashlib import sha256
import secrets
import setup_db


def credential_acquisition():
	"""
	if they'd like to sign up, get their username and password, satisfying
	certain criteria. This function also hashes the supplied password, and adds a salt.
	:returns:
		str: login name
		str: password
		str: the randomly generated salt
	"""

	valid_username_criteria = '^[a-zA-Z0-9]{5,24}$'
	valid_password_criteria = '^[a-zA-Z0-9]{8,24}$'

	# getting the new user's username
	while True:
		login_name = input(
			'Choose a username using at least 5 letters or numbers (max 24 characters): '
		)

		# checking that a username fits the criteria
		while not re.match(valid_username_criteria, login_name):
			login_name = input(
				'Choose a username using at least 5 letters or numbers (max 24 '
				'characters): '
			)

		# comparing against the database to ensure a unique username is chosen
		setup_db.cur.execute(
			'''
				SELECT username 
				FROM users
				WHERE username is ?;
			''', (login_name,)
		)

		duplicate_name = setup_db.cur.fetchall()
		if not duplicate_name:
			break
		else:
			print('Sorry, that username is already taken. Try again!')


	# getting the new user's password
	login_password = input(
		'Choose a password using at least 8 letters or numbers (max 24 characters): '
	)

	# checking that the password fits the criteria
	while not re.match(valid_password_criteria, login_password):
		login_password = input(
			'Choose a password using at least 8 letters or numbers (max 24 characters): '
		)

	# improving security by hashing and salting
	salt = secrets.token_urlsafe(32)
	salted_login_pw = login_password + salt
	hashed_login_pw = sha256(salted_login_pw.encode('utf-8')).hexdigest()


	return login_name, hashed_login_pw, salt


def add_to_database(name, pw, salt):
	"""
	Takes as inputs the return values from the credential_acquisition function and adds
	the name, hashed password, and salt into the database.
	:param name: (str) the supplied username
	:param pw: (str) the hashed password
	:param salt: (str) the randomly generated salt
	:return: no return value.
	"""
	setup_db.cur.execute(
		'''
		INSERT INTO users
		VALUES (?, ?, ?);
		''', (name, pw, salt)
	)
	setup_db.con.commit()
