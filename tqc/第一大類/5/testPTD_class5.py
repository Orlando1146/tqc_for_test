from PYD_class5 import PYD5
import unittest


class test(unittest.TestCase):
    pyd5 = PYD5("or")
    def test_power(self):
        rst = self.pyd5.power(3, 2)
        self.assertEqual(rst,9)

    def test_multiple(self):
        rst=self.pyd5.multiple(2,4)
        self.assertEqual(rst,8)

    def test_is_prime(self):
        rst=self.pyd5.is_prime(11)
        self.assertTrue(rst)

    def test_isnot_prime(self):
        rst=self.pyd5.is_prime(1)
        self.assertFalse(rst)

    def test_fib_less_than_two(self):
        ans=self.pyd5.fib(1)
        self.assertEqual(ans,1)

    def test_fib_more_than_two(self):
        ans=self.pyd5.fib(10)
        self.assertEqual(ans,55)

    def test_quadratic_smaller_than_zero(self):
        ans=self.pyd5.quadratic_equation(9,9,8)
        self.assertEqual(ans,0)

    def test_quadratic_bigger_than_zero(self):
        ans = self.pyd5.quadratic_equation(2,-3,1)
        self.assertEqual(ans, (1.0 , 0.5))

    def test_name(self):
        ans=self.pyd5.compute("english",987,"orlando")
        self.assertEqual(ans,("english",987,"orlando"))

    def test_sum(self):
        ans=self.pyd5.sum(1,10)
        self.assertEqual(ans,55)