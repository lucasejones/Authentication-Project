import setup_db
import hashlib


def log_in():
	"""
	obtains and returns the name and password inputs from the user
	"""

	name = input('enter username: ')
	pw = input('enter password: ')

	return name, pw


def are_valid_credentials(username, password):
	"""
	This function does three things: First, it queries the database for a
	match of the user-input username. Then it obtains and
	formats the hashed password and corresponding salt. Finally, it combines the
	user-input password with the salt, hashes that combination, and compares
	against the database's password.
	:param username: (str) the user-input username to be checked against the
	database
	:param password: (str) the user-input password to be checked against the
	database
	:returns: Bool: True if the user-input credentials match those in the
	database, False if not
	"""

	# querying the database
	setup_db.cur.execute(
		'''
			SELECT * 
			FROM users 
			WHERE username is ?;
		''', (username,)
	)

	# obtaining and formatting the password and salt
	fetched_user_data = setup_db.cur.fetchall()

	formatted_fetched_pw = str(fetched_user_data[0][1]) \
		.replace("'", '') \
		.replace(',', '')
	formatted_fetched_salt = str(fetched_user_data[0][2]) \
		.replace("'", '') \
		.replace(',', '')

	# combining the password and salt and hashing the result
	salted_login_pw = password + formatted_fetched_salt
	hashed_salted_login = hashlib.sha256(salted_login_pw.encode(
		'utf-8')).hexdigest()


	# comparing the result against the database
	return formatted_fetched_pw == hashed_salted_login
		# note that if invalid, we don't say if either one was valid because this would
		# let nefarious actors get additional information.
