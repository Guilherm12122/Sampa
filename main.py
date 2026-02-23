from lexers.lexer import tokenize
from parsers.parser import Parser

code_test_1 = "1+2;1+4"

tokens = tokenize(code_test_1)

# print(tokens)

parser = Parser(tokens)
ast = parser.parse_program()

# print(ast)
