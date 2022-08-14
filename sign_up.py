import re
import sqlite3
import secrets
from hashlib import sha256


def create_db_if_first_user() -> None:
	"""
	If there are no existing users, this creates a local database that contains a table of users
	with columns for their usernames, hashed passwords, and password salts.
	"""
	con = sqlite3.connect('all_users.db')
	cur = con.cursor()
	cur.execute(
		'''
			CREATE TABLE IF NOT EXISTS users (
				username VARCHAR,
				password_hash VARCHAR,
				salt VARCHAR
			);
		'''
	)
	# cur.execute('''SELECT * FROM users''')
	# print(cur.fetchall())  # <-- This is just for quick debugging!
	# definitely do NOT do this in production (haha)...


def check_valid_input_username(intended_username: str) -> bool:
	"""
	checks that the inputted username fits the criteria and returns True if so, False if not.
	"""
	valid_username_criteria = '^[a-zA-Z0-9]{5,24}$'

	if not re.match(valid_username_criteria, intended_username):
		return False
	return True


def check_existing_username(intended_username: str) -> bool:
	"""
	compares the supplied intended username against the database to ensure a unique username is
	chosen. If the user's intended name is already taken, return True. If it's available, return False.
	"""
	con = sqlite3.connect('all_users.db')
	cur = con.cursor()
	cur.execute(
		'''
			SELECT username 
			FROM users
			WHERE username is ?;
		''', (intended_username,)
	)

	duplicate_name = cur.fetchall()
	if duplicate_name:
		return True
	return False


def check_valid_input_password(intended_password: str) -> bool:
	"""
	checks that the inputted password fits the criteria and returns True if so, False if not.
	"""
	valid_password_criteria = '^[a-zA-Z0-9]{8,24}$'

	if not re.match(valid_password_criteria, intended_password):
		return False
	return True


def create_salt() -> str:
	"""
	creates a randomized 32-bit salt that will be used to enhance security.
	"""
	salt = secrets.token_urlsafe(32)
	return salt


def create_hashed_salted_password(password: str, salt: str) -> str:
	"""
	combines the user password with the salt and hashes the result, encrypting it using sha256.
	Returns the hexadecimal hashed result as a string.
	"""
	salted_password = password + salt
	hashed_login_password = sha256(salted_password.encode('utf-8')).hexdigest()
	return hashed_login_password


def add_to_database(name: str, pw: str, salt: str) -> None:
	"""
	Takes as inputs the return values from the credential_acquisition function and adds
	the name, hashed password, and salt into the database.
	:param name: (str) the supplied username
	:param pw: (str) the hashed password
	:param salt: (str) the randomly generated salt
	:return: no return value.
	"""
	con = sqlite3.connect('all_users.db')
	cur = con.cursor()
	cur.execute(
		'''
		INSERT INTO users
		VALUES (?, ?, ?);
		''', (name, pw, salt)
	)
	con.commit()
