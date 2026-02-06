import { isInt, token, isAlpha, isApostrophe, isQuotation, isSkippable, isBinaryOperator, isPrint } from './utils/helpers.js';

//MELHORAIS
// 1 - TALVEZ UTILIZAR DICIONÁRIOS PARA SETAR OS VALORES DE FORMA DINAMICA E REDUZIR O NUMERO DE IFS

function tokenize(sourceCode) {

    const tokens = [];

    let list_stmt = sourceCode.split(';')

    // Enquanto houver statementes
    while (list_stmt.length > 0) {

        // Lista de dicionários que representam um statement
        var dicts_stmt = []

        // Pega o statement
        let stmt = list_stmt[0].split("")

        // Enquanto houver characters no statement
        while (stmt.length > 0) {

            // console.log(stmt[0])

            if (isInt(stmt[0])) {
                 let num = "";
                    while (stmt.length > 0 && isInt(stmt[0])) {
                    num += stmt.shift();
                }

                dicts_stmt.push(token(num, "NUMBER"));
            } else if (isSkippable(stmt[0])) {
                stmt.shift();
            } else if (isBinaryOperator(stmt[0])) {
                switch(stmt[0]) {
                    case "+": dicts_stmt.push(token(stmt.shift(), "PLUS")); break;
                    case "-": dicts_stmt.push(token(stmt.shift(), "MINUS")); break;
                    case "*": dicts_stmt.push(token(stmt.shift(), "MULTIPLICATION")); break;
                    case "/": dicts_stmt.push(token(stmt.shift(), "DIVISION")); break;
                }
            } else if (isPrint(stmt.slice(0, 7).join(''))) {
                dicts_stmt.push(token(stmt.slice(0, 7).join(''), "PRINT"));
                stmt.splice(0, 7);
            }
            else {
                throw new Error(`Unrecognized character found in source: ${stmt[0]}`);
            }
        }

        tokens.push(dicts_stmt);
        list_stmt.shift();

    }
    tokens.push({ value: "EOF", type: "EOF" });
    return tokens;

}

// let code_test_1 = "1+2;1+4";
// let code_test_2 = "MOSTRAR 1+2;MOSTRAR 1+4"
// console.log(tokenize(code_test_1))
// console.log(tokenize(code_test_2))
