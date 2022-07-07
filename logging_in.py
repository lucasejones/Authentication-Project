def log_in():
	'''
	obtains and returns the name and password inputs from the user
	'''

	name = input('enter username: ')
	pw = input('enter password: ')

	# note that if invalid, we don't say if either one was valid because this would
	# let nefarious actors get additional information they could use maliciously.

	return name, pw

