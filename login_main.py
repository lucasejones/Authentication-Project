import re
import logging_in
import sign_up


# prompting the user to decide what action they'd like to take
user_input = input(
	'are you signing up or logging in? Enter "S" for signing up, '
	'or enter "L" for logging in.'
)


# ensuring the user's response is either a valid sign-up or login request
intro_action_pattern = '^[SL]'
while not re.match(intro_action_pattern, user_input) or len(user_input) != 1:
	user_input = input(
		'are you signing up or logging in? Enter "S" for signing up, '
		'or enter "L" for logging in.'
	)


# if the user has chosen to sign up:
if user_input == 'S':
	# acquiring credentials and encrypting
	signup_name, signup_pw, salt = sign_up.credential_acquisition()

	# adding encrypted credentials to database
	sign_up.add_to_database(signup_name, signup_pw, salt)

	print(
		'You\'ve successfully signed up, congratulations! Run the program '
		'again to log in.'
	)


# if the user has chosen instead to log in:
elif user_input == 'L':
	# acquiring name and password user inputs
	login_name, login_pw = logging_in.log_in()

	# granting or denying access to the program
	if logging_in.are_valid_credentials(login_name, login_pw):
		print('You\'re in!')
	else:
		print('Sorry, those credentials are invalid. Please try again.')
