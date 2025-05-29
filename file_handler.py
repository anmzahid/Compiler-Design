
#--------------------------------CSE4803(Assignment 1)----------------------
#created by A N M Zahid Hossain Milkan (200041202)------------------------------
#Date 29 May 2025 (9:30 PM)
def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write_tokens(output_file, tokens):
    with open(output_file, 'w') as f:
        for token in tokens:
            f.write(f"{token['lexeme']}\t{token['name']}\t{token['type']}\t(Line {token['line']})\n")
