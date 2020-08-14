import unittest
from tax import Tax


class TestTax(unittest.TestCase):
    def test_default_tax(self):
        t = Tax()
        self.assertEqual(t.tax(0), 0)
        self.assertEqual(t.tax(10000), 0)
        self.assertEqual(t.tax(10009), 0)
        self.assertEqual(t.tax(10010), 1)
        self.assertEqual(t.tax(12000), 200)
        self.assertEqual(t.tax(56789), 8697)
        self.assertEqual(t.tax(1234567), 473326)


if __name__ == '__main__':
    unittest.main()
