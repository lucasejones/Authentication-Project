import re
import logging_in
import sign_up

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
	signup_name, salt, signup_pw = sign_up.credential_acquisition()

	# # adding encrypted credentials to database
	sign_up.add_to_database(signup_name, signup_pw, salt)


# if the user has chosen instead to log in:
elif signing_up_process is False and logging_in_process is True:
	# acquiring name and password user inputs
	login_name, login_pw = logging_in.log_in()

	# granting or denying access to the program
	if logging_in.are_valid_credentials(login_name, login_pw):
		print('You\'re in!')
	else:
		print('Sorry, those credentials are invalid. Please try again.')
