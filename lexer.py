import ply.lex as lex

# List of tokens
tokens = (
    'VARIABLE_DECLARATION',
    'IF_STATEMENT',
    'FUNCTION_DECLARATION',
    'FUNCTION_DEF',
    'FOR_LOOP',
    'OTHER',
)

# Regular expressions for tokens
t_VARIABLE_DECLARATION = r'(int|char)\s[a-zA-Z_]=(\'[a-zA-Z_0-9]\'|[0-9]+);'
t_IF_STATEMENT = r'if\s*\([^)]*\)\s*{[^}]*}'
t_FUNCTION_DECLARATION = r'(int|void)\s[a-zA-Z_][a-zA-Z_0-9]*\s*\([^)]*\)\s*;'
t_FUNCTION_DEF = r'(int|void)\s[a-zA-Z_][a-zA-Z_0-9]*\s*\([^)]*\)\s*{[^}]*};'
t_FOR_LOOP = r'for\s*\([^)]*\)\s*{[^}]*}'
t_OTHER = r'.'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()