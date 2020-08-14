import unittest
from tax import tax


class TestTax(unittest.TestCase):
    def test_default_tax(self):
        self.assertEqual(tax(0), 0)
        self.assertEqual(tax(10000), 0)
        self.assertEqual(tax(10009), 0)
        self.assertEqual(tax(10010), 1)
        self.assertEqual(tax(12000), 200)
        self.assertEqual(tax(56789), 8697)
        self.assertEqual(tax(1234567), 473326)


if __name__ == '__main__':
    unittest.main()
