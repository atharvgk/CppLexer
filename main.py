from lexer import lexer
from yacc import parser

if __name__ == "__main__":
    code = input("Enter a C++ construct: ")
    
    lexer.input(code)
    token_found = False

    for token in lexer:
        if token.type != 'OTHER':
            token_found = True
            if token.type == 'VARIABLE_DECLARATION':
                print("Valid and Variable Declaration")
            elif token.type == 'IF_STATEMENT':
                print("Valid and If Statement")
            elif token.type == 'FUNCTION_DECLARATION':
                print("Valid and Function Declaration")
            elif token.type == 'FUNCTION_DEF':
                print("Valid and Function Def")
            elif token.type == 'FOR_LOOP':
                print("Valid and For Loop")
    
    if not token_found:
        print("Invalid")
