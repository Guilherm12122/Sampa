from lexers.lexer import tokenize
from parsers.parser import Parser

# code_test_1 = "1+2;1+4"
# code_test_2 = "1+3*5"
# code_test_3 = "1+2*3"
# code_test_4 = "MOSTRAR(1+2*3)"
# code_test_5 = "5 - 1"
# code_test_6 = "1-2*9"

# code_test_7 = "10 / 9"
# code_test_8 = "10 % 9"
code_test_9 = "10 / 9 * 8"

tokens = tokenize(code_test_9)
tokens = tokenize(code_test_9)

print(tokens)

parser = Parser(tokens)
ast = parser.parse_program()
ast_expr = ast[0]
ast_expr_right = ast_expr.right
ast_expr_left = ast_expr.left

# print(ast)
print(ast_expr)
print(ast_expr_right)
print(ast_expr_left)
