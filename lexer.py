# Token class definition to represent tokens
class Token:
    # Token initializer with token type and lexeme
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme
    # Define string rep of Token object    
    def __repr__(self):
        return f"{self.token_type}\t\t{self.lexeme}"

# Lexer function that uses file path and generates tokens
def lexer(file_path):
    with open(file_path, "r") as file:
        source_code = file.read()
# Initialize postion
    position = 0
# Iterate until end is reached    
    while position < len(source_code):
        if source_code[position].isspace():
            position += 1
            continue

        # Keywords
        if source_code[position:].startswith("while"):
            yield Token("keyword", "while")
            position += 5

        # Identifiers
        elif source_code[position].isalpha() or source_code[position] == "_":
            lexeme = source_code[position]
            position += 1
            while source_code[position].isalnum() or source_code[position] == "_":
                lexeme += source_code[position]
                position += 1
            yield Token("identifier", lexeme)

        # Integers and real numbers
        elif source_code[position].isdigit():
            lexeme = source_code[position]
            position += 1
            while source_code[position].isdigit():
                lexeme += source_code[position]
                position += 1

            if source_code[position] == ".":
                lexeme += source_code[position]
                position += 1
                while source_code[position].isdigit():
                    lexeme += source_code[position]
                    position += 1
                yield Token("real", lexeme)
            else:
                yield Token("integer", lexeme)

        # Separators
        elif source_code[position] in "()":
            yield Token("separator", source_code[position])
            position += 1

        # Operators
        elif source_code[position] in "<>=":
            yield Token("operator", source_code[position])
            position += 1

        # Skip Unexpected character
        else:
            position += 1

# Define main that reads input code and writes tokens to seperate file
def main():
    input_file = "input_scode.txt"
    output_file = "output.txt"
# Opens output and writes header
    with open(output_file, "w") as file:
        file.write("token\t\tlexeme\n")
        # Iterate through tokens and write to output
        for token in lexer(input_file):
            file.write(f"{token}\n")


if __name__ == "__main__":
    main()
