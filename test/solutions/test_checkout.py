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
    
    def test_B(self):
        self.assertEqual('B', 30)
    
    def test_BB(self):
        self.assertEqual('BB', 45)

    def test_BBB(self):
        self.assertEqual('BBB', 75)
    
    def test_C(self):
        self.assertEqual('C', 20)
    
    def test_CC(self):
        self.assertEqual('CC', 40)

    def test_D(self):
        self.assertEqual('D', 15)

    def test_DD(self):
        self.assertEqual('DD', 30)
    
if __name__ == '__main__':
    unittest.main()
