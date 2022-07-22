import re
import logging_in
import sign_up

#_____________________________
# __________________________
# toy functions to experiment with unit testing strategy
#_______________________________________________________
def add_these(x: int, y: int) -> int:
	"""takes two numbers and returns their sum"""
	return x + y


def subtract_these(x, y):
	return x - y
#_______________________________________________________


def get_user_desired_action():
	"""
	prompts the user to decide what action they'd like to take: to sign up or log in
	:returns:
		str: 'S' or 'L'
	"""
	user_input_message = input(
		'are you signing up or logging in? Enter "S" for signing up, '
		'or enter "L" for logging in.'
	)
	return user_input_message


def checking_valid_action(user_input):
	"""
	ensures the user's response is either a valid sign-up or login request
	:returns:
		bool: True if the response is valid, False if not
	"""
	valid_action_pattern = '^[SL]'
	if not re.match(valid_action_pattern, user_input) or len(user_input) != 1:
		return False
	return True


if __name__ == '__main__':
	user_decision = get_user_desired_action()
	is_valid_action = checking_valid_action(user_decision)

	while is_valid_action is False:
		user_decision = get_user_desired_action()
		is_valid_action = checking_valid_action(user_decision)



	# if the user has chosen to sign up:
	if user_decision == 'S':
		# acquiring credentials and encrypting
		signup_name, signup_pw, salt = sign_up.credential_acquisition()

		# adding encrypted credentials to database
		sign_up.add_to_database(signup_name, signup_pw, salt)

		print(
			'You\'ve successfully signed up, congratulations! Run the program '
			'again to log in.'
		)


	# if the user has chosen instead to log in:
	elif user_decision == 'L':
		# acquiring name and password user inputs
		login_name, login_pw = logging_in.log_in()

		# granting or denying access to the program
		if logging_in.are_valid_credentials(login_name, login_pw):
			print('You\'re in!')
		else:
			print('Sorry, those credentials are invalid. Please try again.')
