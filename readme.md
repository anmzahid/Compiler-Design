# Lexical Analyzer with Symbol Table and Syntax Error Recovery  
**Created by:** A N M Zahid Hossain Milkan (200041202)  
**Date:** 29 May 2025

---

## Project Overview

This project implements a **lexical analyzer** for a subset of the C language. It tokenizes source code into meaningful tokens, classifies them, manages a symbol table, and performs **syntax checking** with robust **phrase-level error recovery**.

---

## Features

- **Lexical Analysis**:  
  - Tokenizes source code, recognizing keywords, operators, special symbols, constants, identifiers, strings, chars, and preprocessor directives.  
  - Skips comments (single-line `//` and multi-line `/* ... */`).  
  - Classifies tokens by type.

- **Symbol Table Manager**:  
  - Collects and stores identifiers, constants, and relevant tokens with their line numbers.  
  - Prevents duplicate entries.  
  - Allows dumping symbol table contents and saving to file.

- **Syntax Error Handling and Recovery**:  
  - Detects common syntax errors such as:  
    - Missing semicolons  
    - Unbalanced parentheses  
    - Consecutive operands or operators  
    - Extra or misplaced semicolons  
    - Misuse of commas  
    - Incorrect token order  
  - Uses **phrase-level recovery** to fix simple errors automatically, such as:  
    - Inserting missing semicolons  
    - Removing extra semicolons  
    - Replacing misplaced commas with semicolons  
  - Avoids false errors on preprocessor directives (`#include`, etc.)  
  - Maintains a list of all errors found and corrections applied.  
  - Supports **panic mode recovery** to synchronize parsing after errors.

---

## File Descriptions

| File Name               | Purpose                                                                                  |
|------------------------|------------------------------------------------------------------------------------------|
| `main.py`              | Orchestrates the lexical analysis process: reads input file, tokenizes lines, classifies tokens, runs syntax checker, manages symbol table, writes outputs.  |
| `tokenizer.py`         | Tokenizes input lines into a list of tokens, handles string and char literals, skips comments.          |
| `classifier.py`        | Classifies each token into categories: keyword, operator, identifier, constant types, special symbols, etc. |
| `token_types.py`       | Defines token types, regex patterns, keyword/operator/symbol sets used for classification.     |
| `file_handler.py`      | Reads input source file and writes token and error outputs to files.                          |
| `symbol_table_handler.py` | Manages the symbol table: insertion, lookup, dumping, and saving to file.                      |
| `error_recovery.py`    | Implements the robust syntax error handler supporting error reporting and panic mode recovery.  |
| `syntax_checker.py`    | Performs syntax checks on tokenized lines, detects errors, and applies phrase-level recovery fixes. |

---

## How To Use

1. Place your source code to be analyzed in `input.c`.

2. Run the lexical analyzer:

    ```bash
    python main.py
    ```

3. Outputs generated:

   - `output_tokens.txt`: List of tokens with classification and line number.
   - `symbol_table.txt`: Contents of the symbol table with lexemes and token types.
   - `syntax_errors.txt`: Detected syntax errors and any automatic fixes applied.

---

## Example Input

```c
#include <stdio.h>

int main() {
    int x = 10, y = 20;;
    float z = 3.14e-2
    char c = 'a';

    if ((x != y)) {
        z += x * y;;
        printf("Hello\n");
    }

    if (x > 5
        && y < 15)) {
        x = x + + y;
        y 20;
    }

    return 0;
}
