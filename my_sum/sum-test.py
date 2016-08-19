'''DocString of MySumTests'''
import unittest
from my_sum import my_sum

class MySumTests(unittest.TestCase):
	
	def setUp(self):
		self.numbers = [10, 5, 7,8, 90, 60]
			
	def test_sum_of_numbers(self):
		self.assertEqual(my_sum(10,15),25, "Sum")

	def test_non_numbers(self):
		
		self.assertRaises(TypeError, my_sum, 2, 'name')

if __name__ == '__main__':
	unittest.main()
