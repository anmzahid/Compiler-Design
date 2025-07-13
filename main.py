
#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)

#--------------------------------CSE4803(Assignment 2)----------------------
# created by A N M Zahid Hossain Milkan (200041202)
# Integrates Symbol Table and Error Recovery
# main.py

from tokenizer import tokenize, remove_comments
from classifier import classify_token
from file_handler import read_file, write_tokens
from symbol_table import SymbolTable
from robust_syntax_error_handler import RobustSyntaxErrorHandler
from syntax_checker import check_syntax_with_phrase_recovery

def lexical_analyzer(input_file, output_file_tokens, output_file_symbols,       output_file_syntax_errors):
    source_code = ''.join(read_file(input_file))
    clean_code = remove_comments(source_code)
    lines = clean_code.split('\n')

    all_tokens = []
    symbol_table = SymbolTable()
    syntax_error_handler = RobustSyntaxErrorHandler()

    for line_num, line in enumerate(lines, 1):
        token_list_raw = tokenize(line)
        line_tokens = []

        for tok in token_list_raw:
            lexeme, tok_type = classify_token(tok)

            if tok_type in ["IDENTIFIER", "CONSTANT (int)", "CONSTANT (float)", "CONSTANT (char)", "CONSTANT (string)"]:
                symbol_table.insert(lexeme, tok_type, line_num)

            token_info = {'lexeme': lexeme, 'name': tok, 'type': tok_type, 'line': line_num}
            all_tokens.append(token_info)
            line_tokens.append(token_info)

        check_syntax_with_phrase_recovery(line_tokens, line_num, syntax_error_handler)

    write_tokens(output_file_tokens, all_tokens)
    symbol_table.save(output_file_symbols)
    syntax_error_handler.save(output_file_syntax_errors)

    print(symbol_table.dump())
    if syntax_error_handler.has_errors():
        print(syntax_error_handler.dump())
    else:
        print("No syntax errors found.")

if __name__ == "__main__":
    lexical_analyzer("input.c", "output_tokens.txt", "symbol_table.txt", "syntax_errors.txt")
