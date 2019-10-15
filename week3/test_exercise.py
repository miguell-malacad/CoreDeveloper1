import unittest
from fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
	def test_return_fizz(self):
		test_value = 3
		expected_result = "fizz"
		result = fizzbuzz(test_value)
		self.assertEqual(result, expected_result)
		self.assertIsInstance(result, str)

	def test_return_buzz(self):
		test_value = 5
		expected_result = "buzz"
		result = fizzbuzz(test_value)
		self.assertEqual(result, expected_result)
		self.assertIsInstance(result, str)

	def test_return_fizzbuzz(self):
		test_value = 15
		expected_result = "fizzbuzz"
		result = fizzbuzz(test_value)
		self.assertEqual(result, expected_result)
		self.assertIsInstance(result, str)

	def test_return_number(self):
		test_value = 7
		expected_result = str(test_value)
		result = fizzbuzz(test_value)
		self.assertEqual(result, expected_result)
		self.assertIsInstance(result, str)

	def test_input_bulk(self):
		for i in range(1, 101, 1):
			print(fizzbuzz(i))


if __name__ == '__main__':
	unittest.main()
