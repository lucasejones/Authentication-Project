import re
import users


def sign_up_func():
	# if they'd like to sign up, get their username and password with certain
	# constraints
	valid_username_pattern = '^[a-zA-Z0-9]{5,24}$'
	login_name = input(
		'choose a username using at least 5 letters or numbers (max 24 characters): '
	)
	# while not re.match(valid_username_pattern, login_name):
	# 	login_name = input(
	# 		'choose a username using at least 5 letters or numbers (max 24 characters): ')
	while login_name in users.creds:
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

	return login_name, login_password

