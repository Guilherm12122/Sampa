DATA_TYPES = [
    'INTEIRO',
    'STRING',
    'FLUTUANTE',
    'BOOLEANO'
]

KEY_WORDS = [
    'INTEIRO'
]

def check_data_type(stmt, j):

    for dt in DATA_TYPES:

        lenght_dt = len(dt)

        if stmt[j:j+lenght_dt] == dt:

            return dt
        

# def check_data_type(stmt, j):

#     return list(filter(lambda dt : stmt[j:j + len(dt)] == dt, DATA_TYPES))[0]


def check_boolean(stmt, j):

    return stmt[j:j+5] == "FALSO" or stmt[j:j+10] == "VERDADEIRO"
    

def get_identifier(stmt, j):

    identifier = ''

    while j < len(stmt):

        if stmt[j] == '=':
            break

        identifier += stmt[j]

        j += 1

    return identifier, j



def check_identifier(stmt, j):

    identifier = ''

    while j < len(stmt) and (stmt[j].isalnum() or stmt[j] == '_'):

        identifier += stmt[j]
        j += 1

    if identifier not in KEY_WORDS:

        return identifier



def tokenize(code_str: str):
    
    list_stmt = code_str.split(';')

    i = 0
    tokens = []

    while i < len(list_stmt):

        stmt = list_stmt[i]
        tuples_stmt = []
        j = 0

        while j < len(stmt):

            c = stmt[j]

            if check_identifier(stmt, j):

                identifier = check_identifier(stmt, j)

                tuples_stmt.append(('IDENTIFIER', identifier))

                j += len(identifier)

            elif c.isspace():
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
                    tuples_stmt.append(("FLUTUANTE", num))
                else:
                    tuples_stmt.append(("INTEIRO", num))

            elif c == "+":
                tuples_stmt.append(("PLUS", "+"))
                j += 1

            elif c == '-':
                tuples_stmt.append(("MINUS", "-"))
                j += 1

            elif c == '/':
                tuples_stmt.append(("DIVISION", "/"))
                j += 1

            elif c == '%':
                tuples_stmt.append(("MODULUS", "%"))
                j += 1

            elif c == '=':
                tuples_stmt.append(("ASSIGN", "="))
                j += 1

            elif c == "(":
                tuples_stmt.append(("OpenParen", "("))
                j += 1

            elif c == ")":
                tuples_stmt.append(("CloseParam", ")"))
                j += 1

            elif c == "*":
                tuples_stmt.append(("MULTIPLICATION", "*"))
                j += 1

            elif stmt[j:j+2] == '==':
                tuples_stmt.append(("EQUALS", "=="))
                j += 2

            elif stmt[j:j+2] == '!=':
                tuples_stmt.append(("NOT_EQUALS", "!="))
                j += 2

            elif stmt[j:j+7] == "MOSTRAR":
                tuples_stmt.append(("PRINT", "MOSTRAR"))
                j += 7

            elif c in ["'", '"']:

                j += 1

                string = ''

                while j < len(stmt) and stmt[j] != c:

                    string += stmt[j]

                    j += 1

                tuples_stmt.append(('STRING', string))

                j += 1

            elif check_boolean(stmt, j):

                if stmt[j:j+10] == "VERDADEIRO":
                    boolean = "VERDADEIRO"
                else:
                    boolean = "FALSO"

                tuples_stmt.append(('BOOLEAN', boolean))

                j += len(boolean)

            elif check_data_type(stmt, j):

                data_type = check_data_type(stmt, j)

                tuples_stmt.append(('DATA_TYPE', data_type))

                j += len(data_type)

                # if dt:
                    
                #     tuples_stmt.append(dt)

                #     j += leng

                #     identifier, j = get_identifier(stmt, j)

                #     tuples_stmt.append(('IDENTIFIER', identifier.strip()))

            # O que nao for válido anterior, é um identifier (paser vai validar semantica -> tem data type antes ?? tem assing (=) depois??)
            # elif c.isalpha() or c == '_':
            #     identifier = ''

            #     while j < len(stmt) and (stmt[j].isalnum() or stmt[j] == '_'):
            #         identifier += stmt[j]
            #         j += 1

            #     tuples_stmt.append(('IDENTIFIER', identifier))

            else:
                raise Exception(f"Caractere inválido: {c}")
            
        tokens.append(tuples_stmt)
        
        i += 1

    return tokens
