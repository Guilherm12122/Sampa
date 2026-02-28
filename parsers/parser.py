class NumberNode:
    def __init__(self, value):
        self.value = value
    def eval(self, ctx):
        return self.value
    
class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self, ctx):
        return self.left.eval(ctx) + self.right.eval(ctx)
    
class MultiplicativeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self, ctx):
        return self.left.eval(ctx) * self.right.eval(ctx)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stmt_indx = 0
        self.token_indx = 0


    def stmt_at(self):
        return self.tokens[self.stmt_indx] if self.stmt_indx < len(self.tokens) else None
    
    def token_at(self):
        return self.tokens[self.stmt_indx][self.token_indx] if self.token_indx < len(self.tokens[self.stmt_indx]) else None
        
    def shift_token(self):
        tok = self.token_at()
        self.token_indx += 1
        return tok

    def get_token_type(self):
        return self.token_at()[0] if self.token_at() else None
    
    def get_token_value(self):
        return self.token_at()[1] if self.token_at() else None
    

    def parse_add_expr(self):
        
        left = self.parse_multi_expr()

        while (self.get_token_value() in ['+', '-']):

            self.shift_token()

            right = self.parse_multi_expr()

            left = PlusNode(left, right)

        return left
    

    def parse_multi_expr(self):

        left = NumberNode(self.shift_token()[1])

        while (self.get_token_value() in ['*', '%', '/']):

            self.shift_token()

            right = NumberNode(self.shift_token()[1])

            left = MultiplicativeNode(left, right)

        return left



    def parse_statement(self):

        token_type = self.get_token_type()

        match token_type:
            case 'NUMBER':
                return self.parse_add_expr()


    def parse_program(self):

        ast = []

        while self.stmt_at():

            self.token_indx = 0

            while self.token_at():
                ast.append(self.parse_statement())
            self.stmt_indx += 1

        return ast
