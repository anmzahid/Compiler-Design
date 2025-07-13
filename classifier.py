
#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)
# classifier.py (no major changes, just keep as is)

from token_types import *

def classify_token(token):
    if not token.strip():
        return token, "WHITESPACE"

    if token in KEYWORDS:
        return token, "KEYWORD"
    elif token in OPERATORS:
        return token, "OPERATOR"
    elif token in SPECIAL_SYMBOLS:
        return token, "SPECIAL_SYMBOL"
    elif re.fullmatch(INTEGER_PATTERN, token):
        return token, "CONSTANT (int)"
    elif re.fullmatch(FLOAT_PATTERN, token):
        return token, "CONSTANT (float)"
    elif re.fullmatch(CHAR_PATTERN, token):
        return token, "CONSTANT (char)"
    elif re.fullmatch(STRING_PATTERN, token):
        return token, "CONSTANT (string)"
    elif re.fullmatch(PREPROCESSOR_PATTERN, token):
        return token, "PREPROCESSOR"
    elif re.fullmatch(IDENTIFIER_PATTERN, token):
        return token, "IDENTIFIER"
    else:
        return token, "UNKNOWN"
