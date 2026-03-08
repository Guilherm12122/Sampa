from lexers.lexer import tokenize
from parsers.parser import Parser

# code_test_1 = "1+2;1+4"
# code_test_2 = "1+3*5"
code_test_3 = "1+2*3"

# tokens = tokenize(code_test_1)
tokens = tokenize(code_test_3)

# print(tokens)

parser = Parser(tokens)
ast = parser.parse_program()

print(ast)
print(ast[0].right)
print(ast[0].left)
