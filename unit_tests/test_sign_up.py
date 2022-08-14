import sign_up
from sign_up import *
import unittest


class TestCheckValidInputUsername(unittest.TestCase):
	def test_check_valid_input_username_return_type(self):
		self.assertIsInstance(sign_up.check_valid_input_username('Lucas'), bool, 'Should be of '
		'boolean type.')


	def test_check_valid_action_valid_regex(self):
		""" Tests that the function returns true a correct input """
		self.assertTrue(check_valid_input_username('John300'), 'should be True')


	def test_check_valid_action_invalid_regex_short(self):
		""" Tests that the function returns false for an incorrect input """
		self.assertFalse(check_valid_input_username('John'), 'should be False')


	def test_check_valid_action_invalid_regex_long(self):
		""" Tests that the function returns false for an incorrect input """
		self.assertFalse(check_valid_input_username('JohnWithTooManyCharacters'), 'should be False')


	def test_check_valid_action_invalid_regex_special_characters(self):
		""" Tests that the function returns false for an incorrect multiple-character input """
		self.assertFalse(check_valid_input_username('John_!"'), 'should be False')



class TestCheckValidInputPassword(unittest.TestCase):
	def test_check_valid_input_password_return_type(self):
		self.assertIsInstance(sign_up.check_valid_input_password('Lucas'), bool, 'Should be of '
		'boolean type.')


	def test_check_valid_password_valid_regex(self):
		""" Tests that the function returns true a correct input """
		self.assertTrue(check_valid_input_password('John3000'), 'should be True')


	def test_check_valid_password_invalid_regex_short(self):
		""" Tests that the function returns false for an incorrect input """
		self.assertFalse(check_valid_input_password('John300'), 'should be False')


	def test_check_valid_password_invalid_regex_long(self):
		""" Tests that the function returns false for an incorrect input """
		self.assertFalse(check_valid_input_password('JohnWithTooManyCharacters'), 'should be False')


	def test_check_valid_password_invalid_regex_special_characters(self):
		""" Tests that the function returns false for an incorrect multiple-character input """
		self.assertFalse(check_valid_input_password('John_!"'), 'should be False')



class TestCreateSalt(unittest.TestCase):
	def test_create_salt_return_type(self):
		""" Tests that the function returns a string"""
		self.assertIsInstance(sign_up.create_salt(), str, 'Should return a str')



class TestCreateHashedSaltedPassword(unittest.TestCase):
	def test_create_hashed_salted_password_return_type(self):
		""" Tests that the function returns a string"""
		self.assertIsInstance(sign_up.create_hashed_salted_password(
			'John3000', 'AVeqmjgouHbVbiutl2pqtjgg8kY2ryOxd31NycmXuqY'),
			str, 'Should return a str')

	def test_create_hashed_salted_password_return_length(self):
		""" Tests that the function returns a value of length 64, indicating a hexadecimal hash
		using 256 bits, 4 bits per character"""
		self.assertEqual(len(sign_up.create_hashed_salted_password(
			'John3000', 'AVeqmjgouHbVbiutl2pqtjgg8kY2ryOxd31NycmXuqY')),
			64, 'Should be of length 64')



if __name__ == '__main__':
	unittest.main()
