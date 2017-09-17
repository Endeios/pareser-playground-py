'''calculator module'''
from lexer import Lexer
from parser import Parser
from parser import IntNode, PlusNode, MultNode
import logging


class Calculator(object):
    def __init__(self):
        self.log = logging.getLogger("Calculator")
        pass

    def calculate(self, text_input):
        lexer = Lexer(text_input)
        tokens = lexer.tokenize()
        self.log.debug("Tokens: %s" % tokens)
        parser = Parser()
        parser.parse(tokens)
        tree = parser.output
        self.log.debug("Tree is: ")
        self.log.debug(tree)
        return self.make_result(tree)

    def make_result(self, tree):

        if tree is None:
            return 0
        if isinstance(tree, IntNode):
            return tree.value
        elif isinstance(tree, PlusNode):
            return self.make_result(tree.left) + self.make_result(tree.right)
        elif isinstance(tree, MultNode):
            return self.make_result(tree.left) * self.make_result(tree.right)
        else:
            Exception("Unsupported tree")
