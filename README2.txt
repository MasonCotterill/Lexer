The Predictive Parser - README Introduction

Welcome to The Parser project! This program is designed to parse simple arithmetic expressions provided in a text file using a context-free grammar.

Overview

The main objective of this project is to implement a parser function called parse(), which will determine if a given arithmetic expression conforms to the grammar rules defined in the parsing table. The parser should be able to identify and process expressions containing addition, subtraction, multiplication, and parentheses. The parsing process utilizes a stack to control the algorithm flow.

Requirements

To run the program, you need to have one of the following programming language interpreters installed:

Python

Files

The project includes four files:

Prog1.py: The source code of the parser program written in Python.
README.md: This file, explaining how to set up and run the program.

Setup and Execution

Follow these steps to set up and run the program:

    Ensure you have the required interpreter for Python installed on your computer.

    Run Prog1.py using the appropriate command for Python when you're in the same directory as the file. For example:

python3 Prog1.py

The program will read the hard coded input string and print the stack at each insertion. The output will be displayed in the terminal, showing the state of the stack and whether or not the string is accepted.

Review the output in the terminal to see if the input expressions are valid according to the grammar rules. If an expression is valid, the output will indicate "String is accepted/valid." If the expression is not valid, the output will indicate "String is not accepted/invalid."
