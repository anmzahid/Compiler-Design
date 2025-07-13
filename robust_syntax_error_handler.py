# robust_syntax_error_handler.py

class RobustSyntaxErrorHandler:
    def __init__(self):
        self.errors = []
        self.recovering = False

    def report(self, line, message):
        if not self.recovering:
            self.errors.append(f"Line {line}: {message}")
            self.recovering = True

    def recover(self, token):
        # Synchronize on tokens that mark safe resumption points
        if token in [';', '{', '}']:
            self.recovering = False
            return True
        return False

    def has_errors(self):
        return len(self.errors) > 0

    def dump(self):
        lines = ["========== SYNTAX ERRORS =========="]
        lines.extend(self.errors)
        return "\n".join(lines)

    def save(self, filepath):
        with open(filepath, 'w') as f:
            f.write(self.dump())
