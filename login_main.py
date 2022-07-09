import re
import logging_in
import sign_up
import json
import hashlib


# next steps:
	# 1. permanently add each new user to the credentials dict each time
		# there's a successful new signup.
# 			Done! used json to create a users.txt that serves as the database
# 			instead of the previous users.py file. for signup, wrote to this
# 			new users.txt using json.dumps() to create a persistent copy of the
# 			information, and for login, read from users.txt using json.loads().
	# 2. implement hashing
# 			Done! I used hashlib in the login_main file as well as the sign_up
# 			file. Specifically, I chose sha-256 as the hash function.
# 				when registering, the user's password is never stored in
# 			the database, and is instead converted into a hash. (although it
# 			IS stored in a variable until the next user registers, how does
# 			this ultimately affect the security?)
#				when logging in, the user's un-hashed password is hashed,
#				then compared against the hashed value in the database.
		# 2a. add some salt to it!
#			Done! I added salt via the secrets library, recommended by the
#			documentation for cryptographic use cases. The salt is generated
#			upon registration, and stored alongside the hashed password and salt
#			in
#			the database. During login, the salt value is retrieved from the
#			database, appended to the password, and hashed. This value is
#			then compared against the hashed value from the database, and if
#			it matches, the user is granted access.
	# 3. implement 2-factor authentication
	# 4. create some sort of non-bad UI (so anybody could use this)
	# 5. add some actual functionality that's worth having an account and
	# logging in for. consider using an api to grab some information and display
	# it in your new UI as one way to achieve this.

# prompting the user to decide what action they'd like to take
user_input = input(
	'are you signing up or logging in? Enter "S" for signing up, '
	'or enter "L" for logging in.'
)

# ensuring their response is either a valid sign in or login request
intro_action_pattern = '^[SL]'
while not re.match(intro_action_pattern, user_input) or len(user_input) != 1:
	user_input = input(
		'are you signing up or logging in? Enter "S" for signing up, '
		'or enter "L" for logging in.'
	)

if user_input == 'S':
	signing_up_process = True
	logging_in_process = False
elif user_input == 'L':
	signing_up_process = False
	logging_in_process = True


# if the user has chosen to sign up:
if signing_up_process is True and logging_in_process is False:
	# acquiring credentials and encrypting
	signup_name, salt, signup_pw = sign_up.sign_up_func()

	# adding encrypted credentials to database
	sign_up.add_to_database(signup_name, salt, signup_pw)


# if the user has chosen instead to log in:
elif signing_up_process is False and logging_in_process is True:
	login_name, login_pw = logging_in.log_in()

	with open('users.txt', 'r') as file:
		text_data = file.read()
		total_userbase = json.loads(text_data)

	def are_valid_credentials(username, password):
		if username in total_userbase:
			login_salt = total_userbase[username][1]
			salted_login_pw = password + login_salt
			hashed_salted_login = hashlib.sha256(salted_login_pw.encode(
				'utf-8')).hexdigest()
			return total_userbase[username][0] == hashed_salted_login


	# granting access to the program or denying access
	if are_valid_credentials(login_name, login_pw):
		print('You\'re in!')
	else:
		print('Sorry, those credentials are invalid. Please try again.')
