#!/usr/bin/env python3

import os
import sys

def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    """Write content to a file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_cpp_basics_docs():
    """Generate C++ Basics documentation."""
    # Base path for documentation
    base_path = os.path.join('docs', 'cpp-basics')
    create_directory(base_path)

    # Documentation topics with their content
    topics = [
        {
            'filename': 'index.md',
            'content': '''---
layout: default
title: C++ Basics
---

# C++ Basics

An introduction to fundamental C++ programming concepts for beginners.

## Topics

{% assign current_url = page.url %}
{% assign pages_list = site.pages | sort: "title" %}
{% assign has_children = false %}
{% if current_url == "/docs/cpp-basics/" %}
  {% assign current_sections = "Variables and Data Types,Literals and Expressions,Operators,Control Statements" | split: "," %}
  {% assign has_children = true %}
  <ul class="topic-list">
    {% for section in current_sections %}
      <li>
        <a href="{{ site.baseurl }}/docs/cpp-basics/{{ section | downcase | replace: " ", "-" | uri_escape }}">{{ section }}</a>
        <p class="topic-description">Introduction to {{ section | downcase }}</p>
      </li>
    {% endfor %}
  </ul>
{% endif %}

{% if has_children == false %}
<p><em>No subtopics available yet.</em></p>
{% endif %}

<style>
  .topic-list {
    list-style-type: none;
    padding-left: 0;
  }
  .topic-description {
    color: #666;
    margin-left: 20px;
  }
</style>'''
        },
        {
            'filename': 'variables-and-data-types.md',
            'content': '''---
layout: default
title: Variables and Data Types
---

# Variables and Data Types

Variables are containers for storing data values. In C++, each variable must have a specific type that determines what kind of data it can store.

## Basic Data Types

### Integer Types
```cpp
int wholeNumber = 42;          // Stores whole numbers
short smallNumber = 100;       // Smaller range integer
long bigNumber = 1000000L;     // Larger integer
long long hugeNumber = 1LL;    // Very large integer
```

### Floating-Point Types
```cpp
double preciseMeasurement = 3.14159;  // Double-precision decimal
float smallDecimal = 3.14f;           // Single-precision decimal
```

### Character Types
```cpp
char singleLetter = 'A';        // Single character
char asciiCode = 65;            // Character can also store ASCII values
```

### Boolean Type
```cpp
bool isTrue = true;             // Logical true/false value
bool isFalse = false;
```

### String Type
```cpp
string greeting = "Hello, World!";  // Text string (requires #include <string>)
```

## Variable Declaration and Initialization

There are multiple ways to initialize variables:

```cpp
// Direct initialization
int age = 25;

// Constructor initialization
int height(180);

// Uniform initialization (modern C++)
int weight{75};

// Type inference with 'auto'
auto dynamicType = 3.14;  // Compiler determines the type
```

## Constants

```cpp
// Constant values that cannot be changed
const double PI = 3.14159;
const int MAX_USERS = 100;
```

## Type Conversion

```cpp
int intValue = 10;
double doubleValue = static_cast<double>(intValue);  // Explicit type conversion
```

## Best Practices
- Choose the smallest type that can hold your data
- Use meaningful variable names
- Initialize variables when you declare them
- Use `const` for values that shouldn't change

## Common Mistakes to Avoid
- Don't use uninitialized variables
- Be careful with type conversions
- Understand the range of each data type

## Notes
- Always include necessary headers (e.g., `#include <string>` for string)
- Modern C++ encourages type inference with `auto`
- Choose types that accurately represent your data'''
        },
        {
            'filename': 'literals-and-expressions.md',
            'content': '''---
layout: default
title: Literals and Expressions
---

# Literals and Expressions

## Literals

Literals are fixed values directly written in the code:

### Integer Literals
```cpp
// Decimal (base 10)
int decimal = 42;

// Hexadecimal (base 16)
int hex = 0x2A;  // Same as 42

// Binary (base 2)
int binary = 0b101010;  // Also 42

// Long integers
long longValue = 1000000L;

// Unsigned integers
unsigned int positive = 100u;
```

### Floating-Point Literals
```cpp
double pi = 3.14159;
float smallPi = 3.14f;
double scientific = 6.022e23;  // Scientific notation
```

### Character Literals
```cpp
char letter = 'A';
char escape = '\n';  // Newline character
char unicode = u'β';  // Unicode character
```

### String Literals
```cpp
string greeting = "Hello, World!";
string multiline = R"(This is a 
multi-line string)";
```

### Boolean Literals
```cpp
bool truth = true;
bool falsehood = false;
```

## Expressions

Expressions are combinations of values, variables, operators, and function calls that evaluate to a single value:

### Arithmetic Expressions
```cpp
int sum = 5 + 3;          // Addition
int difference = 10 - 4;  // Subtraction
int product = 6 * 7;      // Multiplication
double quotient = 15.0 / 4;  // Division
int remainder = 17 % 5;   // Modulus (remainder)
```

### Compound Expressions
```cpp
int complex = (5 + 3) * 2;  // Parentheses change evaluation order
double mixed = 10 / 4.0 + 2;  // Mixed type expression
```

### Increment and Decrement
```cpp
int x = 5;
int y = x++;   // Post-increment (y = 5, x becomes 6)
int z = ++x;   // Pre-increment (z = 7, x becomes 7)
```

## Type Conversion in Expressions

```cpp
int a = 5;
double b = 2.5;
auto result = a + b;  // Implicit conversion to double
```

## Statements

Statements are complete instructions that perform an action:

```cpp
// Declaration statement
int count = 0;

// Expression statement
count++;

// Compound statement (block)
{
    int temp = count;
    count = temp * 2;
}
```

## Best Practices
- Use parentheses to clarify expression intent
- Be aware of type conversion rules
- Avoid complex expressions that reduce readability
- Use meaningful variable names in expressions

## Common Pitfalls
- Integer division truncates decimal parts
- Be careful with mixed-type expressions
- Understand operator precedence'''
        },
        {
            'filename': 'operators.md',
            'content': '''---
layout: default
title: Operators in C++
---

# Operators in C++

Operators are special symbols that perform operations on variables and values.

## Arithmetic Operators
```cpp
int a = 10, b = 3;

// Basic arithmetic
int sum = a + b;        // Addition: 13
int diff = a - b;       // Subtraction: 7
int prod = a * b;       // Multiplication: 30
double div = a / b;     // Division: 3.333 (integer division)
double preciseDiv = static_cast<double>(a) / b;  // 3.333
int remainder = a % b;  // Modulus (remainder): 1
```

## Comparison Operators
```cpp
bool isEqual = (a == b);     // Equal to: false
bool notEqual = (a != b);    // Not equal to: true
bool greater = (a > b);      // Greater than: true
bool less = (a < b);         // Less than: false
bool greaterEqual = (a >= b);// Greater than or equal: true
bool lessEqual = (a <= b);   // Less than or equal: false
```

## Logical Operators
```cpp
bool x = true, y = false;

bool andOperator = x && y;   // Logical AND: false
bool orOperator = x || y;    // Logical OR: true
bool notOperator = !x;       // Logical NOT: false
```

## Bitwise Operators
```cpp
int bit1 = 5;   // Binary: 0101
int bit2 = 3;   // Binary: 0011

int bitwiseAnd = bit1 & bit2;    // Bitwise AND: 0001 (1)
int bitwiseOr = bit1 | bit2;     // Bitwise OR:  0111 (7)
int bitwiseXor = bit1 ^ bit2;    // Bitwise XOR: 0110 (6)
int bitwiseNot = ~bit1;          // Bitwise NOT: Inverts all bits
int leftShift = bit1 << 1;       // Left shift: 1010 (10)
int rightShift = bit1 >> 1;      // Right shift: 0010 (2)
```

## Assignment Operators
```cpp
int c = 10;

c += 5;   // Same as c = c + 5;  (15)
c -= 3;   // Same as c = c - 3;  (12)
c *= 2;   // Same as c = c * 2;  (24)
c /= 4;   // Same as c = c / 4;  (6)
c %= 3;   // Same as c = c % 3;  (0)
```

## Ternary Operator
```cpp
int max = (a > b) ? a : b;  // If a > b, max = a; otherwise, max = b
```

## Operator Precedence Example
```cpp
int result = 10 + 5 * 2;  // Multiplication happens first: 20
int grouped = (10 + 5) * 2;  // Parentheses change order: 30
```

## Best Practices
- Use parentheses to clarify complex expressions
- Be careful with integer division
- Understand operator precedence
- Use explicit type casting when mixing types

## Common Pitfalls
- Integer division truncates decimal parts
- Bitwise operators work on individual bits
- Logical operators short-circuit
- Be aware of type conversion in mixed expressions'''
        },
        {
            'filename': 'control-statements.md',
            'content': '''---
layout: default
title: Control Statements
---

# Control Statements in C++

Control statements manage the flow of program execution.

## Conditional Statements (If-Else)
```cpp
int age = 20;

// Simple if statement
if (age >= 18) {
    println("You are an adult");
}

// If-else statement
if (age >= 18) {
    println("You can vote");
} else {
    println("You cannot vote yet");
}

// Multiple conditions
if (age < 13) {
    println("Child");
} else if (age < 18) {
    println("Teenager");
} else if (age < 65) {
    println("Adult");
} else {
    println("Senior");
}
```

## Switch Statement
```cpp
int day = 4;

switch (day) {
    case 1:
        println("Monday");
        break;
    case 2:
        println("Tuesday");
        break;
    case 3:
        println("Wednesday");
        break;
    case 4:
        println("Thursday");
        break;
    case 5:
        println("Friday");
        break;
    case 6:
        println("Saturday");
        break;
    case 7:
        println("Sunday");
        break;
    default:
        println("Invalid day");
}
```

## While Loops
```cpp
// Basic while loop
int count = 0;
while (count < 5) {
    println("Count:", count);
    count++;
}

// Do-while loop (always executes at least once)
do {
    println("This runs at least once");
    count++;
} while (count < 10);
```

## For Loops
```cpp
// Standard for loop
for (int i = 0; i < 5; i++) {
    println("Iteration:", i);
}

// Range-based for loop (modern C++)
Array<int> numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    println("Number:", num);
}

// Nested loops
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        println("i:", i, "j:", j);
    }
}
```

## Loop Control Statements
```cpp
// Break statement
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;  // Exits the loop completely
    }
    println("Current:", i);
}

// Continue statement
for (int i = 0; i < 5; i++) {
    if (i == 2) {
        continue;  // Skips rest of the current iteration
    }
    println("Current:", i);
}
```

## Nested Conditionals
```cpp
int x = 10, y = 20;

if (x > 0) {
    if (y > 0) {
        println("Both x and y are positive");
    } else {
        println("x is positive, but y is not");
    }
} else {
    println("x is not positive");
}
```

## Best Practices
- Use meaningful conditions
- Keep conditional logic simple and readable
- Prefer switch for multiple conditions on a single variable
- Use break and continue sparingly
- Consider early returns in functions to reduce nesting

## Common Pitfalls
- Forgetting break in switch statements
- Infinite loops
- Unintended fall-through in switch statements
- Complex nested conditionals'''
        }
    ]

    # Write each topic to a file
    for topic in topics:
        file_path = os.path.join(base_path, topic['filename'])
        write_file(file_path, topic['content'])

    print(f"Generated C++ Basics documentation in {base_path}")

def main():
    """Main function to run the documentation generator."""
    generate_cpp_basics_docs()

if __name__ == "__main__":
    main()