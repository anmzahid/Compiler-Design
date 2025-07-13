import re
from token_types import OPERATORS, SPECIAL_SYMBOLS, SINGLE_LINE_COMMENT, MULTI_LINE_COMMENT

COMPOSITE_TOKENS = sorted(list(OPERATORS | SPECIAL_SYMBOLS), key=lambda x: -len(x))

def remove_comments(text):
    text = re.sub(SINGLE_LINE_COMMENT, '', text)
    text = re.sub(MULTI_LINE_COMMENT, '', text)
    return text

def tokenize(line):
    tokens = []
    i = 0
    length = len(line)

    while i < length:
        ch = line[i]

        if ch.isspace():
            i += 1
            continue

        # String literal
        if ch == '"':
            start = i
            i += 1
            while i < length and (line[i] != '"' or line[i-1] == '\\'):
                i += 1
            i += 1
            tokens.append(line[start:i])
            continue

        # Char literal
        if ch == "'":
            start = i
            i += 1
            while i < length and (line[i] != "'" or line[i-1] == '\\'):
                i += 1
            i += 1
            tokens.append(line[start:i])
            continue

        # Match composite operators/symbols
        matched = False
        for symbol in COMPOSITE_TOKENS:
            if line[i:i+len(symbol)] == symbol:
                tokens.append(symbol)
                i += len(symbol)
                matched = True
                break
        if matched:
            continue

        # Number (int or float with exponent)
        number_match = re.match(r'\d+(\.\d*)?([eE][-+]?\d+)?', line[i:])
        if number_match:
            token = number_match.group()
            tokens.append(token)
            i += len(token)
            continue

        # Identifier or preprocessor directives (start with letter, _, or #)
        if re.match(r'[a-zA-Z_#]', ch):
            token = ''
            while i < length and re.match(r'[a-zA-Z0-9_]', line[i]):
                token += line[i]
                i += 1
            tokens.append(token)
            continue

        # Otherwise, single char token
        tokens.append(ch)
        i += 1

    return tokens


# Debugging test block
if __name__ == "__main__":
    demo = '''
#include <stdio.h>
int main() {
    float z = 3.14e-2;
    /* comment block */
    return 0;
}
'''
    print("Original code:")
    print(demo)

    clean = remove_comments(demo)
    print("\nCode after removing comments:")
    print(clean)

    for line in clean.split('\n'):
        print(f"LINE: {line}")
        print(f"TOKENS: {tokenize(line)}")
