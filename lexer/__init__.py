'''lexer for numbers expressions'''
import re
from enum import Enum
from collections import namedtuple


class TokenType(Enum):
    INT = 1
    PLUS = 2
    MULT = 3
    LPAR = 4
    RPAR = 5


Token = namedtuple("Token", "type text")


def regexes(reg_tuple):
    return (reg_tuple[0], re.compile(reg_tuple[1]))


TOKEN_DEFINITIONS = [
    (TokenType.INT, "\A(\d+)"),
    (TokenType.PLUS, "\A(\+)"),
    (TokenType.MULT, "\A(\*)"),
    (TokenType.LPAR, "\A(\()"),
    (TokenType.RPAR, "\A(\))")
]


class Lexer(object):
    def __init__(self, text):
        self.data = text
        self.token_searchers = map(regexes, TOKEN_DEFINITIONS)

    def tokenize(self):
        text = self.data.strip()
        tokens = []
        while len(text) is not 0:
            match_rule = False
            for token_definition in self.token_searchers:
                matches = token_definition[1].match(text)
                if(matches):
                    token_text = matches.group(0)
                    text = text[len(token_text):].strip()
                    tokens.append(Token(token_definition[0], token_text))
                    match_rule = True
            if(match_rule is False):
                raise Exception("Could not match the %s" % text)
        return tokens
