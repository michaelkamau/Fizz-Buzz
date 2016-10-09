import unittest
from fizz_buzz.fizzbuzz import fizz_buzz


class FizzBuzzOutcomes(unittest.TestCase):
    def test_fizzbuzz_returns_correct_fizz(self):
        """
        Fizzbuzz should return Fizz if the arg is divisible by 3 only
        """
        self.assertEqual('Fizz', fizz_buzz(9))

    def test_fizzbuzz_returns_correct_buzz(self):
        """
        Fizzbuzz should return Buzz if the arg is divisible by 5 only
        """
        self.assertEqual('Buzz', fizz_buzz(100))

    def test_fizzbuzz_returns_correct_fizzbuzz(self):
        """
        Fizzbuzz should return FizzBuzz if the arg is divisible by both 3 and 5 only
        """
        self.assertEqual('FizzBuzz', fizz_buzz(15))

    def test_fizzbuzz_returns_original_arg(self):
        """
        Fizzbuzz should return the arg passed if it is not divisible by both 3 and 5
        """
        self.assertEqual(34, fizz_buzz(34))


if __name__ == '__main__':
    unittest.main()
