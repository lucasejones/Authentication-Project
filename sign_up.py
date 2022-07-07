import re
import json
from hashlib import sha256


def sign_up_func():
	'''
	if they'd like to sign up, get their username and password with
	certain constraints.
	:returns:
		str: login name
		str: password

	'''

	valid_username_pattern = '^[a-zA-Z0-9]{5,24}$'
	login_name = input(
		'choose a username using at least 5 letters or numbers (max 24 characters): '
	)

	total_userbase = {}
	with open('users.txt', 'r') as file:
		text_data = file.read()
		total_userbase = json.loads(text_data)

	while login_name in total_userbase:
		login_name = input(
			'Sorry, that username is already taken. Try again!: '
		)
	while not re.match(valid_username_pattern, login_name):
		login_name = input(
			'choose a username using at least 5 letters or numbers (max 24 characters): '
		)

	valid_password_pattern = '^[a-zA-Z0-9]{8,24}$'
	login_password = input(
		'choose a password using at least 8 letters or numbers (max 24 characters): '
	)
	while not re.match(valid_password_pattern, login_password):
		login_password = input(
			'choose a password using at least 8 letters or numbers (max 24 characters): '
		)

	hashed_login_pw = sha256(login_password.encode('utf-8')).hexdigest()

	return login_name, hashed_login_pw

