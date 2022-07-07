import re
import logging_in
import sign_up
import json
from hashlib import sha256

# next steps:
	# 1. permanently add each new user to the credentials dict each time
		# there's a successful new signup.
# 			Done! used json to create a users.txt that serves as the database
# 			instead of the previous users.py file. for signup, wrote to this
# 			new users.txt using json.dumps() to create a persistent copy of the
# 			information, and for login, read from users.txt using json.loads().
	# 2. implement hashing
# 			Done! used hashlib in the login_main file as well as the sign_up
# 			file.
# 				when registering, the user's password is never stored in
# 			the database, and is instead converted into a hash. (although it
# 			IS stored in a variable until the next user registers, how does
# 			this ultimately affect the security?)
#				when logging in, the user's un-hashed password is hashed,
#				then compared against the hashed value in the database.
		# 2a. add some salt to it!
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

# 1. when user signs up, store their pw as a hash in the database
# 2. when user logs in, take their un-hashed pw, hash it, and check against
# the database in the valid creds function

# if the user has chosen to sign up:
if signing_up_process is True and logging_in_process is False:
	signup_name, signup_pw = sign_up.sign_up_func()

	with open('users.txt') as json_file:
		decoded_userbase = json.load(json_file)

	decoded_userbase[signup_name] = signup_pw

	with open('users.txt', 'w') as file:
		file.write(json.dumps(decoded_userbase))

	print('You\'ve successfully signed up, congratulations! Run the program '
		'again to log in.')


# if the user has chosen instead to log in:
elif signing_up_process is False and logging_in_process is True:
	login_name, login_pw = logging_in.log_in()

	total_userbase = {}
	with open('users.txt', 'r') as file:
		text_data = file.read()
		total_userbase = json.loads(text_data)

	def are_valid_credentials(username, password):
		if username in total_userbase:
			hashed_pw = sha256(password.encode('utf-8')).hexdigest()
			return total_userbase[username] == hashed_pw

	# granting access to the program or denying access
	if are_valid_credentials(login_name, login_pw):
		print('You\'re in!')
	else:
		print('Sorry, those credentials are invalid. Please try again.')
