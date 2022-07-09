import sqlite3

con = sqlite3.connect('ppab6.db')

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
print(cur.fetchall())

# prints the entire users table
cur.execute('''SELECT * FROM users''')
print(cur.fetchall())

# cur.execute('''
# 	SELECT password_hash
# 	FROM users
# 	WHERE username is ?
# ''', ('Garry',))
# print(cur.fetchall())