import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(checkout('E'), -1)

    def test_empty(self):
        self.assertEqual(checkout(''), 0)

    def test_A(self):
        self.assertEqual(checkout('A'), 50)
    
    def test_AA(self):
        self.assertEqual(checkout('AA'), 100)
    
    def test_AAA(self):
        self.assertEqual(checkout('AAA'), 130)

    def test_AAAA(self):
        self.assertEqual(checkout('AAAA'), 180)
    
    def test_B(self):
        self.assertEqual(checkout('B'), 30)
    
    def test_BB(self):
        self.assertEqual(checkout('BB'), 45)

    def test_BBB(self):
        self.assertEqual(checkout('BBB'), 75)
    
    def test_C(self):
        self.assertEqual(checkout('C'), 20)
    
    def test_CC(self):
        self.assertEqual(checkout('CC'), 40)

    def test_D(self):
        self.assertEqual(checkout('D'), 15)

    def test_DD(self):
        self.assertEqual(checkout('DD'), 30)
    
if __name__ == '__main__':
    unittest.main()
