'''main test suite'''
import unittest
from lexer_test import TestLexerApp
from parser_test import TestParserApp
from calculator_test import TestCalculatorApp
import logging

logging.basicConfig(
    format='[%(name)s](%(levelname)s) : %(message)s',
    level=logging.INFO)


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLexerApp))
    test_suite.addTest(unittest.makeSuite(TestParserApp))
    test_suite.addTest(unittest.makeSuite(TestCalculatorApp))
    return test_suite


mySuit = suite()


runner = unittest.TextTestRunner()
runner.run(mySuit)
