---
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
char escape = '
';  // Newline character
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
- Understand operator precedence