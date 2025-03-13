---
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
- Be aware of type conversion in mixed expressions