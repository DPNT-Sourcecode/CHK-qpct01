import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(checkout('1'), -1)

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

    def test_AAAAA(self):
        self.assertEqual(checkout('AAAAA'), 200)

    def test_AAAAAA(self):
        self.assertEqual(checkout('AAAAAA'), 250)
    
    def test_AABAAAA(self):
        self.assertEqual(checkout('AABAAAA'), 280)
    
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
    
    def test_E(self):
        self.assertEqual(checkout('E'), 40)
    
    def test_EE(self):
        self.assertEqual(checkout('EE'), 80)
    
    def test_EBE(self):
        self.assertEqual(checkout('EBE'), 80)

    def test_EBEB(self):
        self.assertEqual(checkout('EBEB'), 110)

    def test_EEE(self):
        self.assertEqual(checkout('EEE'), 120)
    
    def test_F(self):
        self.assertEqual(checkout('F'), 10)
    
    def test_FF(self):
        self.assertEqual(checkout('FF'), 20)
    
    def test_FFF(self):
        self.assertEqual(checkout('FFF'), 20)
    
    def test_FFFF(self):
        self.assertEqual(checkout('FFFF'), 30)
    
    def test_FFFFF(self):
        self.assertEqual(checkout('FFFFF'), 40)
    
    def test_FFFFFF(self):
        self.assertEqual(checkout('FFFFFF'), 40)
    
    def test_FFFFFFF(self):
        self.assertEqual(checkout('FFFFFFF'), 50)
    
if __name__ == '__main__':
    unittest.main()
