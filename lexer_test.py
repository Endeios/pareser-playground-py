'''Lexer Tests'''
import unittest
from lexer import Lexer
from lexer import TokenType


class TestLexerApp(unittest.TestCase):
    '''main test case'''

    def assertTokenizesTo(self, input_text, expected):
        lexer = Lexer(input_text)
        actual = lexer.tokenize()
        self.assertEqual(expected, actual)

    def setUp(self):
        '''set up tests'''

    def test_empty(self):
        self.assertTokenizesTo("", [])

    def test_number(self):
        self.assertTokenizesTo("500", [(TokenType.INT, "500")])

    def test_plus(self):
        self.assertTokenizesTo("+", [(TokenType.PLUS, "+")])

    def test_times(self):
        self.assertTokenizesTo("*", [(TokenType.MULT, "*")])

    def test_sum(self):
        self.assertTokenizesTo(
            "1+1",
            [(TokenType.INT, "1"),
             (TokenType.PLUS, "+"),
             (TokenType.INT, "1")])

    def test_mult(self):
        self.assertTokenizesTo(
            "1*1",
            [(TokenType.INT, "1"),
             (TokenType.MULT, "*"),
             (TokenType.INT, "1")])

    def test_complex_mult(self):
        self.assertTokenizesTo(
            "1*1+1",
            [(TokenType.INT, "1"),
             (TokenType.MULT, "*"),
             (TokenType.INT, "1"),
             (TokenType.PLUS, "+"),
             (TokenType.INT, "1")])

    def test_wrong_input(self):
        with self.assertRaises(Exception):
            self.assertTokenizesTo(
                "1x1+1",
                [(TokenType.INT, "1"),
                 (TokenType.MULT, "*"),
                 (TokenType.INT, "1"),
                 (TokenType.PLUS, "+"),
                 (TokenType.INT, "1")])


if __name__ == "__main__":
    unittest.main()
