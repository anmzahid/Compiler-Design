#--------------------------------CSE4803(Assignment 2)----------------------
# created by A N M Zahid Hossain Milkan (200041202)
# Symbol Table Manager

class SymbolTableEntry:
    def __init__(self, lexeme, token_type, line_no):
        self.lexeme = lexeme
        self.token_type = token_type
        self.line_no = line_no

    def __repr__(self):
        return f"{self.lexeme} ({self.token_type}) at line {self.line_no}"

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, lexeme, token_type, line_no):
        # Only store identifiers, constants, etc.
        if lexeme not in self.symbols:
            self.symbols[lexeme] = SymbolTableEntry(lexeme, token_type, line_no)

    def lookup(self, lexeme):
        return self.symbols.get(lexeme, None)

    def dump(self):
        return "\n".join([str(entry) for entry in self.symbols.values()])

    def save(self, filepath):
        with open(filepath, 'w') as f:
            f.write(self.dump())
