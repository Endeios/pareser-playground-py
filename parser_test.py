'''Tests'''
import unittest
from lexer import Lexer
from mathparser import Parser
from mathparser import IntNode, PlusNode, MultNode
import logging


log = logging.getLogger("Test")


def printtree(tree, comment="expected"):
    log.debug("%s -> %s" % (comment, tree))


class TestParserApp(unittest.TestCase):
    '''main test case'''

    def setUp(self):
        '''set up tests'''

    def test_sempty(self):
        self.assertCompilesToTree("", None)

    def test_one(self):
        self.assertCompilesToTree("1", IntNode(1))

    def test_ssimple_sum(self):
        self.assertCompilesToTree("2+1", PlusNode(IntNode(2), IntNode(1)))

    def stest_simple_sum_2(self):
        self.assertCompilesToTree(
            "2+1+3",
            PlusNode(
                PlusNode(
                    IntNode(2),
                    IntNode(1)),
                IntNode(3)))

    def test_simple_mult(self):
        self.assertCompilesToTree("3*5", MultNode(IntNode(3), IntNode(5)))

    def test_simple_mult_2(self):
        self.assertCompilesToTree(
            "3*5+1",
            PlusNode(
                MultNode(
                    IntNode(3),
                    IntNode(5)),
                IntNode(1)))

    def assertCompilesToTree(self, input_text, expected_tree):
        lexer = Lexer(input_text)
        tokens = lexer.tokenize()
        parser = Parser()
        printtree(expected_tree)
        parser.parse(tokens)
        tree = parser.output
        printtree(tree, "actual")
        self.assertEqual(expected_tree, tree)


if __name__ == "__main__":
    unittest.main()
