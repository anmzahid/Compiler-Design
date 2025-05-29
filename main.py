
#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)

from tokenizer import tokenize, remove_comments
from classifier import classify_token
from file_handler import read_file, write_tokens

def lexical_analyzer(input_file, output_file):
    lines = read_file(input_file)
    all_tokens = []

    for line_num, line in enumerate(lines, 1):
        clean_line = remove_comments(line)
        token_list = tokenize(clean_line)
        for tok in token_list:
            lexeme, tok_type = classify_token(tok)
            all_tokens.append({
                'lexeme': lexeme,
                'name': tok,
                'type': tok_type,
                'line': line_num
            })

    write_tokens(output_file, all_tokens)

if __name__ == "__main__":
    lexical_analyzer("input.c", "output_tokens.txt")
