The Lexer - README
Introduction

Welcome to The Lexer project! This program is designed to tokenize simple C++ source code provided in a text file. 

Overview

The main objective of this project is to implement a lexer function called lexer(), which will return a token and its corresponding lexeme when called. The lexer should be able to identify tokens for identifiers, integers, and other tokens defined ad-hoc. The Finite State Automaton (FSA) is used to recognize these tokens.
Requirements

To run the program, you need to have one of the following programming language compilers or interpreters installed:

    C++
    Python

Files

The project includes five files:

    input_scode.txt: Contains the simple C++ source code to be tokenized by the lexer.
    FSA_mydesign.doc: A document containing the regular expressions and the corresponding FSA design for the required tokens (identifier and integer).
    lexer_program: The source code of the lexer program written in one of the allowed programming languages (C, C++, Java, or Python).
    output: A file containing the output of the lexer, listing the tokens and their corresponding lexemes.
    README.md: This file, explaining how to set up and run the program.

Setup and Execution

Follow these steps to set up and run the program:

    Ensure you have the required compiler or interpreter for your chosen programming language installed on your computer.

    Place the input_scode.txt file in the same directory as the lexer_program.

    Compile (if required) and run the lexer_program using the appropriate command for your chosen programming language. For example:
        For Python: python lexer_program.py

    The program will read the input_scode.txt file and tokenize the source code. The output will be saved in a new file called output in the same directory as the program.

    Open the output file to see the resulting tokens and their corresponding lexemes in two columns.
 
