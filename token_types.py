
#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)
import re

# ----------------------------
# 1. Keywords (C89/C90 subset)
# ----------------------------
KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else',
    'enum', 'extern', 'float', 'for', 'goto', 'if', 'inline', 'int', 'long', 'register',
    'restrict', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
    'union', 'unsigned', 'void', 'volatile', 'while', '_Bool', '_Complex', '_Imaginary'
}

# ----------------------------
# 2. Operators
# ----------------------------
ARITHMETIC_OPERATORS = {'+', '-', '*', '/', '%'}
RELATIONAL_OPERATORS = {'<', '>', '<=', '>=', '==', '!='}
LOGICAL_OPERATORS = {'&&', '||', '!'}
BITWISE_OPERATORS = {'&', '|', '^', '~', '<<', '>>'}
ASSIGNMENT_OPERATORS = {'=', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>='}
INCREMENT_DECREMENT = {'++', '--'}
TERNARY_OPERATOR = {'?' , ':'}

# Group all operators
OPERATORS = (
    ARITHMETIC_OPERATORS |
    RELATIONAL_OPERATORS |
    LOGICAL_OPERATORS |
    BITWISE_OPERATORS |
    ASSIGNMENT_OPERATORS |
    INCREMENT_DECREMENT |
    TERNARY_OPERATOR
)

# ----------------------------
# 3. Special Symbols
# ----------------------------
SPECIAL_SYMBOLS = {
    '(', ')', '{', '}', '[', ']', ';', ',', '.', '->', '...', '#', '##'
}

# ----------------------------
# 4. Constants and Literals
# ----------------------------

# Identifiers: variable/function/array names
IDENTIFIER_PATTERN = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

# Integer literals (decimal, octal, hexadecimal)
INTEGER_PATTERN = re.compile(r'^(0[xX][0-9a-fA-F]+|0[0-7]*|\d+)([uU]?[lL]{0,2})?$')

# Floating-point literals (with optional exponent and suffix)
FLOAT_PATTERN = re.compile(r'^(\d*\.\d+|\d+\.\d*)([eE][-+]?\d+)?[fFlL]?$')

# Character literal (with escape characters)
CHAR_PATTERN = re.compile(r"^'(\\.|[^\\'])'$")

# String literal (with escape characters)
STRING_PATTERN = re.compile(r'^"(\\.|[^"\\])*"$')

# ----------------------------
# 5. Preprocessor Directives
# ----------------------------
PREPROCESSOR_PATTERN = re.compile(r'^#\s*\w+')

# ----------------------------
# 6. Comments (not tokenized but useful to skip)
# ----------------------------

# Single-line: // comment
SINGLE_LINE_COMMENT = re.compile(r'//.*')

# Multi-line: /* comment */
MULTI_LINE_COMMENT = re.compile(r'/\*.*?\*/', re.DOTALL)
