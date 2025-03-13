---
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
- Choose types that accurately represent your data