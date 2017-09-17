'''Tests'''
import unittest
from calculator import Calculator
import logging


log = logging.getLogger("Test")


class TestCalculatorApp(unittest.TestCase):
    '''main test case'''

    def setUp(self):
        '''set up tests'''

    def xtest_calculator_empty(self):
        self.assert_result_is("", 0)

    def xtest_calculator_1(self):
        self.assert_result_is("1", 1)

    def test_calculator_sum(self):
        self.assert_result_is("3+1", 4)

    def test_calculator_prod(self):
        self.assert_result_is("3*2", 6)

    def test_calculator_prod_sum1(self):
        self.assert_result_is("3*2+1", 7)

    def test_calculator_prod_sum2(self):
        self.assert_result_is("1+3*2", 7)

    def test_calculator_prod_prod3(self):
        self.assert_result_is("3*3*3", 27)

    def assert_result_is(self, input_string, expected_result):
        calculator = Calculator()
        result = calculator.calculate(input_string)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
