import sqlite3


def get_login_username() -> str:
	"""
	obtains and returns the name input from the user
	"""
	name = input('enter username: ')
	return name


def get_login_password() -> str:
	"""
	obtains and returns the password input from the user
	"""
	pw = input('enter password: ')
	return pw


def find_user(username: str) -> list:
	# querying the database for the user
	con = sqlite3.connect('all_users.db')
	cur = con.cursor()
	cur.execute(
		'''
			SELECT * 
			FROM users 
			WHERE username is ?;
		''', (username,)
	)

	fetched_user_data = cur.fetchall()
	return fetched_user_data


def format_fetched_password(fetched_user_data: list) -> str:
	"""
	takes the password from the fetched user data and modifies the string to be usable for
	comparison later
	"""
	formatted_fetched_pw = str(fetched_user_data[0][1]) \
		.replace("'", '')
	return formatted_fetched_pw


def format_fetched_salt(fetched_user_data: list) -> str:
	"""
	takes the salt from the fetched user data and modifies the string to be usable for
	comparison later
	"""
	formatted_fetched_salt = str(fetched_user_data[0][2]) \
		.replace("'", '')
	return formatted_fetched_salt


def compare_fetched_pw_to_input_pw(formatted_fetched_pw: str, input_password: str) \
		-> bool:
	"""
	compares the encrypted inputted password against the encrypted database password.
	returns True if they match, False if they don't.
	"""
	return formatted_fetched_pw == input_password
