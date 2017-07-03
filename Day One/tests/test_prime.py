import unittest
from prime import Prime


class TestsPrime(unittest.TestCase):
    def setUp(self):
        self.prime = Prime()

    def test_returns_list(self):
        self.assertIsInstance(self.prime.check(5), list)
        
    def test_one(self):
        self.assertIn(1, self.prime.check(6))

    def test_zero(self):
        self.assertIn(0, self.prime.check(6))

    def test_number_is_prime(self):
        self.assertEquals(self.prime.check(6), [2, 3, 5])

    def test_error_if_arg_not_int(self):
        self.assertRaises(TypeError, self.prime.check, 'two')

if __name__ == '__main__':
    unittest.main()