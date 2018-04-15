import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual('E', -1)

    def test_empty(self):
        self.assertEqual('', 0)

    def test_A(self):
        self.assertEqual('A', 50)
    
    def test_AA(self):
        self.assertEqual('A', 100)
    
    def test_AAA(self):
        self.assertEqual('A', 130)

    def test_AAAA(self):
        self.assertEqual('A', 180)


if __name__ == '__main__':
    unittest.main()
