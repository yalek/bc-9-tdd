"""This class tests the sum of the function super_sum"""
import unittest
from super_sum import super_sum

class MySuperSumTest(unittest.TestCase):
	def test_list_has_string(self):
		self.assertEqual('invalid data type', super_sum('2',2))

	def test_single_digit_super_sum(self):
		'''Returns the sum of the single digits in the list'''
		self.assertEqual(4, super_sum(2,2), msg = "The sum of numbers")
		self.assertEqual(6, super_sum(2,2,2), msg = "The sum of numbers  ")
		

	def test_list_is_empty(self):
		self.assertEqual('list empty', super_sum())

	def test_double_digit_super_sum(self):
		'''Returns the sum of the double digits in the list'''
		self.assertEqual(110, super_sum(10, 20, 80), msg = "The sum numbers in list")
		self.assertEqual(60, super_sum(35, 25), msg = "The sum numbers in list")

	def test_single_digit_list(self):
		'''Returns the sum of the single digits and and those in the list'''
		self.assertEqual(10, super_sum(2, 2, [2,2,2]), msg = "The sum numbers in the list")
		self.assertEqual(14, super_sum(2, 3, 1, [2,1,5]), msg = "The sum numbers in the list")

	def test_double_digit_list(self):
		'''Returns the sum of the double digit numbers and those in the list'''
		self.assertEqual(190, super_sum(20, 30, [20, 40, 80]), msg = "The sum numbers in the list")
		self.assertEqual(290, super_sum(80, 90, 10, [10, 30, 60, 10]), msg = "The sum numbers in the list")

	def test_mixed_digits(self):
		'''Returns the sum of the mixed numbers in the lists'''
		self.assertEqual(922, super_sum(2, 400, [20, 500]), msg = "The sum numbers in the list")
		self.assertEqual(4003, super_sum(1000, 3000,[1,1,1]), msg = "The sum numbers in the list")

if __name__ == "__main__":
	unittest.main()


