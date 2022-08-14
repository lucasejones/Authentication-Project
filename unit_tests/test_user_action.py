from user_action import *
import unittest


class TestGetUserDesiredAction(unittest.TestCase):
	def test_get_user_desired_action_return_type(self):
		""" Tests that the function does indeed return user input as a string """
		self.assertIsInstance(get_user_desired_action(), str, 'Should be a str')



class TestCheckValidAction(unittest.TestCase):
	def test_check_valid_action_return_type(self):
		""" Tests that the function return value is boolean type """
		self.assertIsInstance(check_valid_action('S'), bool, 'should be a bool')


	def test_check_valid_action_valid_regex(self):
		""" Tests that the function returns true a correct input """
		self.assertTrue(check_valid_action('L'), 'should be True')


	def test_check_valid_action_invalid_regex(self):
		""" Tests that the function returns false for an incorrect single-character input """
		self.assertFalse(check_valid_action('n'), 'should be False')


	def test_check_valid_action_invalid_regex_multiple_characters(self):
		""" Tests that the function returns false for an incorrect multiple-character input """
		self.assertFalse(check_valid_action('SL'), 'should be False')


if __name__ == '__main__':
	unittest.main()
