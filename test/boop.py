import os

# Define the base directory
base_dir = "docs/cpp-intro"

# Dictionary with section content using indented code blocks in Markdown
sections = {
    "variables": """---
layout: default
title: Variables
---

# Variables

Variables are named storage locations in memory that hold values. In C++, you must declare a variable’s type before using it.

## Declaring Variables

    int age = 25;        // Integer variable
    double salary = 55000.50;  // Floating-point variable
    char grade = 'A';    // Character variable

Variables can be modified after declaration:

    age = 26;  // Updates the value of age
""",
    "types": """---
layout: default
title: Data Types
---

# Data Types

C++ provides various data types to store different kinds of values.

## Basic Types
- `int`: Stores whole numbers (e.g., 42)
- `float`: Stores single-precision decimals (e.g., 3.14)
- `double`: Stores double-precision decimals (e.g., 3.14159)
- `char`: Stores single characters (e.g., 'x')
- `bool`: Stores true or false

Example:

    int count = 10;
    float temp = 23.5;
""",
    "literals": """---
layout: default
title: Literals
---

# Literals

Literals are fixed values written directly in code.

## Examples
- Integer: `42`, `0xFF` (hexadecimal)
- Floating-point: `3.14`, `2.5e-3` (scientific notation)
- Character: `'a'`, `'\n'` (newline)
- String: `"Hello, world!"`

Usage:

    int x = 100;      // Integer literal
    double y = 9.8;   // Floating-point literal
""",
    "expressions-and-statements": """---
layout: default
title: Expressions and Statements
---

# Expressions and Statements

An **expression** computes a value, while a **statement** performs an action.

## Examples

    int x = 5 + 3;    // Expression: 5 + 3 evaluates to 8
    x = x * 2;        // Statement: Assigns new value to x
""",
    "operators": """---
layout: default
title: Operators
---

# Operators

Operators perform operations on values and variables.

## Types
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `&&`, `||`, `!`

Example:

    int a = 10, b = 5;
    int sum = a + b;      // 15
    bool isEqual = a == b;  // false
""",
    "control-statements": """---
layout: default
title: Control Statements
---

# Control Statements

Control statements direct the flow of a program.

## Examples

    int x = 10;
    if (x > 0) {
        println("Positive");  // Conditional execution
    }

    for (int i = 0; i < 5; i++) {
        println(i);  // Loops 0 to 4
    }
""",
    "functions": """---
layout: default
title: Functions
---

# Functions

Functions are reusable blocks of code that perform specific tasks.

## Example

    int add(int a, int b) {
        return a + b;
    }

    int main() {
        int result = add(3, 4);  // result = 7
        return 0;
    }
"""
}

def create_files():
    # Ensure the base directory exists
    os.makedirs(base_dir, exist_ok=True)

    # Create each section folder and its index.md file
    for section, content in sections.items():
        # Define the folder path
        folder_path = os.path.join(base_dir, section)
        os.makedirs(folder_path, exist_ok=True)

        # Define the file path
        file_path = os.path.join(folder_path, "index.md")

        # Write the content to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())

        print(f"Created {file_path}")

if __name__ == "__main__":
    create_files()