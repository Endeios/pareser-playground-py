'''Parser module'''
from lexer import TokenType
from copy import deepcopy
import logging
from collections import namedtuple

IntNode = namedtuple("IntNode", "value")
PlusNode = namedtuple("PlusNode", "left right")
MultNode = namedtuple("MultNode", "left right")


class Parser(object):
    def __init__(self):
        '''initilizes a parser'''
        self.output = None
        self.log = logging.getLogger("Parser")

    def parse(self, tokens):
        '''parses a token list'''
        self.tokens = deepcopy(tokens)
        self.tokens.reverse()
        return self.expression()

    # E->E+E | int <=> E->int Ei
    #                  Ei -> +Ei | 0
    def expression(self):
        self.log.debug("Starting Expression: %s" % self.tokens)
        if len(self.tokens) is 0:
            return
        else:
            self.product()
            self.expression_i()

    def expression_i(self):
        if len(self.tokens) is 0:
            return
        elif self.peek(TokenType.PLUS):
            self.pop(TokenType.PLUS)
            lhs = self.output
            self.product()
            self.output = PlusNode(lhs, self.output)
            self.expression_i()
        else:
            raise Exception(
                "Could not finish the expression: %s" %
                self.expression)

    def product(self):
        if len(self.tokens) is 0:
            return
        else:
            self.terminal()
            self.product_i()

    def product_i(self):
        if len(self.tokens) is 0:
            return
        elif self.peek(TokenType.MULT):
            self.pop(TokenType.MULT)
            lhs = self.output
            self.terminal()
            self.output = MultNode(lhs, self.output)
            self.product_i()
        else:
            return

    def terminal(self):
        value = int(self.pop(TokenType.INT))
        self.output = IntNode(value)

    def pop(self, expected_type):
        self.log.debug("Popping for %s in %s" % (expected_type, self.tokens))
        new_token = self.tokens.pop()
        if(new_token.type == expected_type):
            return new_token.text
        else:
            raise Exception(
                "Wrong token type: i was expecting %s and i got %s"
                % (expected_type, new_token.type))

    def peek(self, node_type, offset=0):
        self.log.debug("Peeking for %s in %s" % (node_type, self.tokens))
        try:
            return self.tokens[len(self.tokens) - offset - 1].type == node_type
        except BaseException:
            return False
