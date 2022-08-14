import sqlite3


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
