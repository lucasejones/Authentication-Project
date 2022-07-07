
def log_in():
	name = input('enter username: ')
	pw = input('enter password: ')

	# function that authenticates user
	# note that if invalid, we don't say if either one was valid because this would
	# let nefarious actors get additional information they could use maliciously.

	# print(are_valid_credentials(name, pw))
	return name, pw

