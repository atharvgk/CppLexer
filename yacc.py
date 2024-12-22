import ply.yacc as yacc
from lexer import tokens

# Parser rules
def p_construct(p):
    '''
    construct : VARIABLE_DECLARATION
              | IF_STATEMENT
              | FUNCTION_DECLARATION
              | FUNCTION_DEF
              | FOR_LOOP
              | OTHER
    '''
    pass  # Do nothing for now

# Error handling in parser
def p_error(p):
    print("Invalid construct")

# Build the parser
parser = yacc.yacc()
