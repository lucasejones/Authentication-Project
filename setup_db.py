import sqlite3

con = sqlite3.connect('ppab6-test.db')

cur = con.cursor()

# shows the name of all tables in the db
cur.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
print(cur.fetchall())

# prints the entire users table
cur.execute('''SELECT * FROM users''')
print(cur.fetchall())



