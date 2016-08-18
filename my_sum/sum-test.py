import unittest
from my_sum import my_sum

class MySumTests(unittest.TestCase):
	
	def setUp(self):
		self.numbers = [10, 5, 7,8, 90, 60]
	
		'''DocString of MySumTests'''
		
	def test_sum_of_numbers(self):
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(my_sum(10,15),25, "Sum")

	def test_diff_of_number(self):
		self.assertEqual(my_sum(15,10),5, "Difference")

	'''Assert throwing of exception when it's a number'''
	def test_non_numbers(self):
		self.assertTrue(my_sum(''), "please input intergers")

		pass


if __name__ == '__main__':
	unittest.main()


		