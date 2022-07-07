import re
import logging_in
import sign_up
import users

# next steps:
	# 1. permanently add each new user to the credentials dict each time
		# there's a successful new signup.

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


# if the user has chosen to sign up
if signing_up_process is True and logging_in_process is False:
	signup_name, signup_pw = sign_up.sign_up_func()

	# function that adds new users to the "database"
	def add_to_creds(username, password):
		users.creds[username] = password


	# adding the new user to the "database"
	add_to_creds(signup_name, signup_pw)
	# print(creds) <- definitely don't do this in production hahaha...
	print(users.creds)
	print('You\'ve successfully signed up, congratulations! Run the program '
		'again to log in.')

# if the user has chosen instead to log in
elif signing_up_process is False and logging_in_process is True:
	login_name, login_pw = log_in()

	def are_valid_credentials(username, password):
		if username in users.creds:
			if users.creds[username] == password:
				return True
		return False

	# granting access to the program or denying access
	if are_valid_credentials(login_name, login_pw):
		print('You\'re in!')
	else:
		print('Sorry, those credentials are invalid. Please try again.')
