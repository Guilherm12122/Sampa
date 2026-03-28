DATA_TYPES = [
    'INTEIRO',
    'STRING',
    'FLUTUANTE',
    'BOOLEANO'
]

KEY_WORDS = ['SE', 'SENAO'] + DATA_TYPES

def list_into_string(lst):

    return ''.join(lst)


def get_token_len(token):

    return len(token[1])


def check_data_type(stmt, j):

    for dt in DATA_TYPES:

        lenght_dt = len(dt)
        print(stmt[j:j+lenght_dt])

        if list_into_string(stmt[j:j+lenght_dt]) == dt:

            return dt


def check_boolean(stmt, j):

    check_false = list_into_string(stmt[j:j+5]) == "FALSO"
    check_true = list_into_string(stmt[j:j+10]) == "VERDADEIRO"

    return check_false or check_true
    

def get_identifier(stmt, j):

    identifier = ''

    while j < len(stmt):

        if stmt[j] == '=':
            break

        identifier += stmt[j]

        j += 1

    return identifier, j

def get_identifier_or_datatype(stmt, j):

    check_nat = ''

    while j < len(stmt) and (stmt[j].isalnum() or stmt[j] == '_'):

        check_nat += stmt[j]
        j += 1

    if check_nat and check_nat not in KEY_WORDS:

        return ('IDENTIFIER', check_nat)
    
    elif check_nat in DATA_TYPES:

        return ('DATA_TYPE', check_nat)



def tokenize(code_str: str):
    
    stmt = list(code_str)

    j = 0
    tokens = []

    while j < len(stmt):

        c = stmt[j]

        if c.isspace():
            j += 1

        elif c.isdigit():
            num = ""
            has_dot = False

            while j < len(stmt) and (stmt[j].isdigit() or stmt[j] == '.'):
                if stmt[j] == '.':
                    if has_dot:
                        raise Exception("Float malformado")
                    has_dot = True
                num += stmt[j]
                j += 1

            if has_dot:
                tokens.append(("FLUTUANTE", num))
            else:
                tokens.append(("INTEIRO", num))

        elif c == "+":
            tokens.append(("PLUS", "+"))
            j += 1

        elif c == '-':
            tokens.append(("MINUS", "-"))
            j += 1

        elif c == '/':
            tokens.append(("DIVISION", "/"))
            j += 1

        elif c == '%':
            tokens.append(("MODULUS", "%"))
            j += 1

        elif c == '=':
            tokens.append(("ASSIGN", "="))
            j += 1

        elif c == "(":
            tokens.append(("OpenParen", "("))
            j += 1

        elif c == ")":
            tokens.append(("CloseParam", ")"))
            j += 1

        elif c == "*":
            tokens.append(("MULTIPLICATION", "*"))
            j += 1

        elif list_into_string(stmt[j:j+2]) == '==':
            tokens.append(("EQUALS", "=="))
            j += 2

        elif list_into_string(stmt[j:j+2]) == '!=':
            tokens.append(("NOT_EQUALS", "!="))
            j += 2

        elif list_into_string(stmt[j:j+7]) == "MOSTRAR":
            tokens.append(("PRINT", "MOSTRAR"))
            j += 7

        elif c in ["'", '"']:

            j += 1

            string = ''

            while j < len(stmt) and stmt[j] != c:

                string += stmt[j]

                j += 1

            tokens.append(('STRING', string))

            j += 1

        elif check_boolean(stmt, j):

            if list_into_string(stmt[j:j+10]) == "VERDADEIRO":
                boolean = "VERDADEIRO"
            else:
                boolean = "FALSO"

            tokens.append(('BOOLEAN', boolean))

            j += len(boolean)

        else:
            
            undef = get_identifier_or_datatype(stmt, j)

            if not undef:

                raise Exception(f"Caractere inválido: {c}")
            
            tokens.append(undef)

            j += get_token_len(undef)

    return tokens
