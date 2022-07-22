import login_main
import unittest


class TestAdd(unittest.TestCase):
	def test_add_these(self):
		"""
		Test that it can sum a typical hypothetical input
		"""
		self.assertEqual(login_main.add_these(1, 10), 11, 'Should be 11')


	def test_add_these_negatives(self):
		"""
		Test that it can sum negatives
		"""
		self.assertEqual(login_main.add_these(-1, -10), -11, 'Should be -11')


	def test_add_these_strings(self):
		"""
		Test that it only accepts arguments of type int
		"""
		self.assertIsInstance(login_main.add_these('house', 'car'), int, 'not type '
																			'int')

	# def test_add_these_bools(self):
	# 	"""
	# 	Test that it rejects arguments of type bool (bool is a subclass of int)
	# 	"""
	# 	self.assertIsInstance(login_main.add_these(True, False), int, 'not type int')


# class TestSubtract(unittest.TestCase):
# 	def test_subtract_these(self):
# 		self.assertEqual(login_main.subtract_these(6, 2), 4, 'Should be 4')
#
# 	def test_subtract_strings(self):
# 		self.assertIsInstance(login_main.subtract_these('car', 'house'), 10,
# 		'Should be of type int')


if __name__ == '__main__':
	unittest.main()


