from token_types import OPERATORS, SPECIAL_SYMBOLS, SINGLE_LINE_COMMENT, MULTI_LINE_COMMENT
import re

# Combine all multi-char operators/symbols to check first
COMPOSITE_TOKENS = sorted(
    list(OPERATORS | SPECIAL_SYMBOLS),
    key=lambda x: -len(x)  # longest match first
)

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

        # Handle string literals
        if ch == '"':
            start = i
            i += 1
            while i < length and (line[i] != '"' or line[i-1] == '\\'):
                i += 1
            i += 1
            tokens.append(line[start:i])
            continue

        # Handle char literals
        if ch == "'":
            start = i
            i += 1
            while i < length and (line[i] != "'" or line[i-1] == '\\'):
                i += 1
            i += 1
            tokens.append(line[start:i])
            continue

        # Try to match longest composite operator/symbol
        matched = False
        for symbol in COMPOSITE_TOKENS:
            if line[i:i+len(symbol)] == symbol:
                tokens.append(symbol)
                i += len(symbol)
                matched = True
                break
        if matched:
            continue

        # Match identifier, number, etc.
        token = ''
        while i < length and re.match(r'\w', line[i]):
            token += line[i]
            i += 1
        if token:
            tokens.append(token)
        else:
            # For unknown single characters
            tokens.append(ch)
            i += 1

    return tokens

#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)