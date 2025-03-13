---
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
- Complex nested conditionals