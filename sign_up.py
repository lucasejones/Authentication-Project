import re
import json
from hashlib import sha256
import secrets


def sign_up_func():
	'''
	if they'd like to sign up, get their username and password under
	certain criteria.
	:returns:
		str: login name
		str: password

	'''

	# getting the new user's username
	valid_username_pattern = '^[a-zA-Z0-9]{5,24}$'
	login_name = input(
		'choose a username using at least 5 letters or numbers (max 24 characters): '
	)

	# checking against the database to ensure a unique username is chosen
	total_userbase = {}
	with open('users.txt', 'r') as file:
		text_data = file.read()
		total_userbase = json.loads(text_data)

	while login_name in total_userbase:
		login_name = input(
			'Sorry, that username is already taken. Try again!: '
		)

	# checking that a username fits the criteria
	while not re.match(valid_username_pattern, login_name):
		login_name = input(
			'choose a username using at least 5 letters or numbers (max 24 characters): '
		)

	# getting the new user's password
	valid_password_pattern = '^[a-zA-Z0-9]{8,24}$'
	login_password = input(
		'choose a password using at least 8 letters or numbers (max 24 characters): '
	)

	# checking that the password fits the criteria
	while not re.match(valid_password_pattern, login_password):
		login_password = input(
			'choose a password using at least 8 letters or numbers (max 24 characters): '
		)

	# improving security by hashing and salting
	salt = secrets.token_urlsafe(32)
	salted_login_pw = login_password + salt
	hashed_login_pw = sha256(salted_login_pw.encode('utf-8')).hexdigest()


	return login_name, salt, hashed_login_pw


'''
if even more security is needed, consider using the password-based key
derivation function to benefit from iterations of the hashed and salted 
password: 

salt = secrets.token_bytes(32)
plaintext = login_password.encode('utf-8')
iterations = 10000
dk = hashlib.pbkdf2_hmac('sha256', plaintext, salt, iterations)
hashed_and_salted_login_pw = dk.hex()
'''
