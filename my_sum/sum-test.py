import unittest
from my_sum import my_sum

class MySumTests(unittest.TestCase):
	
	def setUp(self):
		self.numbers = [10, 5, 7,8, 90, 60]
	
		'''DocString of MySumTests'''
		
	def test_sum_of_numbers(self):
		result = my_sum(5,10)
		self.assertNotEquals(result, 20)
		self.assertEqual(my_sum(10,15),25, "Sum")

	'''Assert throwing of exception when it's a number'''
	def test_non_numbers(self):
		#self.assertTrue(my_sum(''), "please input intergers")
		self.assertRaises(TypeError, my_sum, 2, 'name')

		#pass


if __name__ == '__main__':
	unittest.main()


		