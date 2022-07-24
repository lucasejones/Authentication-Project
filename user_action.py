import re


def get_user_desired_action() -> str:
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


def check_valid_action(user_input: str) -> bool:
	"""
	ensures the user's response is either a valid sign-up or login request
	:returns:
		bool: True if the response is valid, False if not
	"""
	valid_action_pattern = '^[SL]'
	if not re.match(valid_action_pattern, user_input) or len(user_input) != 1:
		return False
	return True
