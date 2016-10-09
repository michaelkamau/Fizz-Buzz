import unittest
from fizz_buzz.fizzbuzz import fizzbuzz


class FizzBuzzOutcomes(unittest.TestCase):
    def test_fizzbuzz_returns_correct_fizz(self):
        """
        Fizzbuzz should return Fizz if the arg is divisible by 3 only
        """
        self.assertEqual('Fizz', fizzbuzz(9))

    def test_fizzbuzz_returns_correct_buzz(self):
        """
        Fizzbuzz should return Buzz if the arg is divisible by 5 only
        """
        self.assertEqual('Buzz', fizzbuzz(100))


if __name__ == '__main__':
    unittest.main()
