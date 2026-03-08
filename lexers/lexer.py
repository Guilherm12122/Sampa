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

            if c.isspace():
                j += 1

            elif c.isdigit():
                num = ""
                while j < len(stmt) and stmt[j].isdigit():
                    num += stmt[j]
                    j += 1
                tuples_stmt.append(("NUMBER", int(num)))

            elif c == "+":
                tuples_stmt.append(("PLUS", "+"))
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

            elif stmt[j:j+7] == "MOSTRAR":
                tuples_stmt.append(("PRINT", "MOSTRAR"))
                j += 7

            else:
                raise Exception(f"Caractere inválido: {c}")
            
        tokens.append(tuples_stmt)
        
        i += 1

    return tokens

