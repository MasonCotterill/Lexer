# Defining the Parsing table for the grammar given for this assignment
table = {
    'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
    'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
    'T': {'a': ['F', 'R'], '(': ['F', 'R']},
    'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
    'F': {'a': ['a'], '(': ['(', 'E', ')']}
}

# Initializing the stack with $ representing end of string
stack = ['$']

# Hardcoding the input string
hard_str = "(a+a)*a"

# Defining the parsing function
def parse(hard_str):
    # Adding start symbol to the stack
    stack.append('E')
    # Initialize input string index with 0
    index = 0
    # Iterate until stack empties
    while len(stack) > 0:
        # Find the top element of the stack
        top = stack[-1]
        # If the top is equal to the current input take the input
        if top == hard_str[index]:
            print(f"Stack: {stack}  Input: {hard_str[index:]} ")
            stack.pop()
            index += 1
        # If the top element is terminal but doesn't match the input print the current stack and current input
        elif top in ('a', '+', '-', '*', '/', '(', ')', '$'):
            print(f"Stack: {stack}  Input: {hard_str[index:]} ")
            return False
        # If the top element is a non-terminal, use a production rule and replace it
        else:
            try:
                # Look up production rule in parsing table
                production = table[top][hard_str[index]]
                print(f"Stack: {stack}  Input: {hard_str[index:]}  ")

                # Replace the non-terminal with symbol from production rule
                stack.pop()
                for symbol in reversed(production):
                    if symbol != 'ε':
                        stack.append(symbol)
            except KeyError:
                # If no production rule is found push error
                print(f"Stack: {stack}  Input: {hard_str[index:]} ")
                return False
    # If the stack is empty, the input string is valid
    return True

# Call the parsing function with hardcoded input string
if parse(hard_str + '$'):
    #if parsing was successful print valid
    print("String is accepted/valid.")
else:
    #if parsing was unsuccessful print invalid
    print("String is not accepted/invalid.")
