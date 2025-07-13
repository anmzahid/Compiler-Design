# syntax_checker.py

def try_phrase_level_corrections(tokens, i, line_num, error_handler):
    """
    Attempts simple phrase-level fixes at token index i.
    Returns (tokens, new_index, fixed) where fixed=True if correction done.
    """
    token = tokens[i]['lexeme']
    tok_type = tokens[i]['type']

    # Insert missing semicolon at end of statement (except preprocessor lines)
    if i == len(tokens) - 1 and token not in [';', '{', '}']:
        # Don't insert semicolon if line starts with preprocessor (#)
        if len(tokens) > 0 and tokens[0]['lexeme'] == '#':
            # No fix needed for preprocessor lines
            return tokens, i, False

        error_handler.errors.append(f"Line {line_num}: Missing semicolon inserted at end.")
        semicolon_token = {'lexeme': ';', 'name': ';', 'type': 'SPECIAL_SYMBOL', 'line': line_num}
        tokens.append(semicolon_token)
        return tokens, i, True

    # Remove extra semicolon if two consecutive semicolons
    if token == ';' and i + 1 < len(tokens) and tokens[i + 1]['lexeme'] == ';':
        error_handler.errors.append(f"Line {line_num}: Extra semicolon removed.")
        tokens.pop(i)
        return tokens, max(i - 1, 0), True

    # Replace comma with semicolon if likely statement terminator
    if token == ',' and (i + 1 == len(tokens) or tokens[i + 1]['lexeme'] in ['int', 'float', 'char', 'if', 'return']):
        error_handler.errors.append(f"Line {line_num}: Replaced comma with semicolon.")
        tokens[i]['lexeme'] = ';'
        tokens[i]['name'] = ';'
        tokens[i]['type'] = 'SPECIAL_SYMBOL'
        return tokens, i, True

    # Add more phrase-level fixes as needed here...

    return tokens, i, False


def check_syntax_with_phrase_recovery(tokens, line_num, error_handler):
    stack = []
    prev_token_type = None

    i = 0
    length = len(tokens)
    while i < length:
        token = tokens[i]['lexeme']
        tok_type = tokens[i]['type']

        if error_handler.recovering:
            if error_handler.recover(token):
                i += 1
                continue
            else:
                i += 1
                continue

        if token == '(':
            stack.append('(')
        elif token == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                error_handler.report(line_num, "Unmatched closing parenthesis ')'")

        if tok_type in ["IDENTIFIER", "CONSTANT (int)", "CONSTANT (float)", "CONSTANT (char)", "CONSTANT (string)"]:
            current_type = "operand"
        elif tok_type == "OPERATOR":
            current_type = "operator"
        else:
            current_type = "special"

        if prev_token_type == current_type and current_type in ("operand", "operator"):
            error_handler.report(line_num, f"Consecutive {current_type}s: '{tokens[i-1]['lexeme']}' and '{token}'")

        # Try phrase-level corrections before moving on
        tokens, i, fixed = try_phrase_level_corrections(tokens, i, line_num, error_handler)
        if fixed:
            length = len(tokens)
            if not error_handler.recovering:
                prev_token_type = None
            continue

        prev_token_type = current_type
        i += 1

    if stack:
        error_handler.report(line_num, "Unbalanced opening parenthesis '('")

    # Check statement end token for missing semicolon (skip preprocessor lines)
    if length > 0:
        first_token = tokens[0]['lexeme']
        last_token = tokens[-1]['lexeme']
        if first_token != '#' and last_token not in [';', '{', '}']:
            tokens, _, fixed = try_phrase_level_corrections(tokens, length - 1, line_num, error_handler)
            if not fixed:
                error_handler.report(line_num, "Missing semicolon at end of statement")
