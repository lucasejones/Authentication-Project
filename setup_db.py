import sqlite3

if __name__ == '__main__':
	con = sqlite3.connect('all_users.db')
	cur = con.cursor()

	cur.execute('''
	CREATE TABLE IF NOT EXISTS users (
	username VARCHAR,
	password_hash VARCHAR,
	salt VARCHAR
	);
	''')

	# cur.execute('''
	# DROP TABLE users;
	# ''')

	# shows the name of all tables in the db
	cur.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
	# print(cur.fetchall())

	# prints the entire users table
	# cur.execute('''SELECT * FROM users''')
	# print(cur.fetchall()) #<-- definitely don't do this in production hahaha...
