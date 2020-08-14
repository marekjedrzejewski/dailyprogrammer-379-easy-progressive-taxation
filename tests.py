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

    def test_default_overall_rate(self):
        t = Tax()
        self.assertGreaterEqual(t.overall_rate(0), 0)
        self.assertLessEqual(t.overall_rate(0), 10009)
        self.assertEqual(t.overall_rate(0.06), 25000)
        self.assertEqual(t.overall_rate(0.09), 34376)
        self.assertEqual(t.overall_rate(0.32), 256250)
        self.assertEqual(t.overall_rate(0.40), None)


if __name__ == '__main__':
    unittest.main()
