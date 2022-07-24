import user_action
import logging_in
import sign_up


if __name__ == '__main__':

	# obtaining a valid action from the user
	while True:
		user_desired_action = user_action.get_user_desired_action()
		is_valid_action = user_action.check_valid_action(user_desired_action)
		if is_valid_action is True:
			break

	# if the user has chosen to sign up:
	if user_desired_action == 'S':
		sign_up.create_db_if_first_user()

		# obtaining a valid and unique username
		while True:
			input_username = sign_up.get_input_username()
			if sign_up.check_valid_input_username(input_username) is False:
				print('Sorry, that username is invalid. Try again!')
				continue
			if sign_up.check_existing_username(input_username) is True:
				print('Sorry, that username is already taken. Try again!')
				continue
			break

		# obtaining a valid password
		while True:
			input_password = sign_up.get_input_password()
			if sign_up.check_valid_input_password(input_password) is True:
				break
			print('Sorry, that password is invalid. Try again!')

		# improving security by salting and hashing the password
		salt = sign_up.create_salt()
		hashed_login_pw = sign_up.create_hashed_salted_password(input_password, salt)
		sign_up.add_to_database(input_username, hashed_login_pw, salt)

		print(
			'You\'ve successfully signed up, congratulations! Run the program '
			'again to log in.'
		)

	# if the user has chosen instead to log in:
	elif user_desired_action == 'L':
		# acquiring name and password user inputs
		login_name = logging_in.get_login_username()
		login_pw = logging_in.get_login_password()

		# obtaining user data from the database
		found_user_data = logging_in.find_user(login_name)

		# if the username is in the database then format the data, encrypt the supplied password,
		# and compare it for validity.
		if len(found_user_data) == 1:
			formatted_found_password = logging_in.format_fetched_password(found_user_data)
			formatted_found_salt = logging_in.format_fetched_salt(found_user_data)
			encrypted_input_password = sign_up.create_hashed_salted_password(login_pw,
				formatted_found_salt)
			valid_credentials = logging_in.compare_fetched_pw_to_input_pw(formatted_found_password,
				encrypted_input_password)

			if valid_credentials:
				print('You\'re in!')
			else:
				print('Sorry, those credentials are invalid. Please try again.')
		else:
			print('Sorry, those credentials are invalid. Please try again')
