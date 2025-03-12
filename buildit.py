#!/usr/bin/env python3
import os
import shutil
import sys

def create_file(path, content):
    """Creates a file with the specified content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {path}")

def setup_github_pages_repository():
    """Sets up a GitHub Pages repository for 'Deploy from a branch' method."""
    # Create base directories
    for dir_path in [
        "docs",
        "docs/_layouts",
        "docs/_includes",
        "docs/assets/css",
        "docs/assets/js",
        "docs/cpp-intro",
        "docs/cpp-intro/arrays",
        "docs/cpp-intro/arrays/creating",
        "docs/cpp-intro/arrays/accessing",
        "docs/cpp-intro/arrays/modifying",
        "docs/cpp-intro/arrays/loops",
        "docs/cpp-intro/arrays/patterns"
    ]:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Create _config.yml
    config_content = """title: "Computer Science Courses"
description: "Course materials for CS classes"
baseurl: "/programming"
url: "https://mssmcs.github.io"

# Build settings
theme: jekyll-theme-cayman
permalink: pretty

# Default layout settings
defaults:
  -
    scope:
      path: ""
    values:
      layout: "default"
"""
    create_file("docs/_config.yml", config_content)
    
    # Create default layout
    default_layout = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }} | {{ site.title }}</title>
  <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
  <style>
    .content {
      max-width: 1000px;
      margin: 0 auto;
      padding: 20px;
    }
    pre {
      background-color: #f6f8fa;
      border-radius: 6px;
      padding: 16px;
      overflow: auto;
    }
    code {
      font-family: monospace;
    }
    .navigation {
      background-color: #f0f0f0;
      padding: 10px;
      margin-bottom: 20px;
      border-radius: 5px;
    }
    .navigation a {
      margin-right: 15px;
      text-decoration: none;
    }
    .navigation a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <header class="page-header" role="banner">
    <h1 class="project-name">{{ site.title }}</h1>
    <h2 class="project-tagline">{{ site.description }}</h2>
  </header>
  
  <main class="content">
    <div class="navigation">
      <a href="{{ site.baseurl }}/">Home</a>
      <a href="{{ site.baseurl }}/cpp-intro/">C++ Introduction</a>
      <a href="{{ site.baseurl }}/cpp-intro/arrays/">Array Class</a>
    </div>
    
    <h1>{{ page.title }}</h1>
    
    {{ content }}
  </main>
  
  <footer class="site-footer">
    <p>Maintained by MSSM CS Department</p>
  </footer>
</body>
</html>
"""
    create_file("docs/_layouts/default.html", default_layout)
    
    # Create home layout
    home_layout = """---
layout: default
---
{{ content }}
"""
    create_file("docs/_layouts/home.html", home_layout)
    
    # Create custom CSS
    custom_css = """/* Custom CSS overrides */
.highlight pre {
  background-color: #272822;
  color: #f8f8f2;
}
"""
    create_file("docs/assets/css/style.scss", """---
---

@import "{{ site.theme }}";
""" + custom_css)
    
    # Create main index page
    main_index = """---
layout: home
title: Home
---

# Computer Science Courses

Welcome to the course materials for CS classes.

## Available Resources

- [C++ Introduction]({{ site.baseurl }}/cpp-intro/)
  - [Array Class Documentation]({{ site.baseurl }}/cpp-intro/arrays/)
"""
    create_file("docs/index.md", main_index)
    
    # Create cpp-intro index
    cpp_intro_index = """---
layout: default
title: C++ Introduction
---

# Introduction to C++

This section contains resources for learning C++ programming.

## Available Topics

- [Array Class]({{ site.baseurl }}/cpp-intro/arrays/)
"""
    create_file("docs/cpp-intro/index.md", cpp_intro_index)
    
    # Create array index page
    array_index = """---
layout: default
title: Working with the Array Class
---

# Working with the Array Class

This guide introduces the `Array<>` class, a beginner-friendly alternative to the standard C++ vector. The `Array<>` class provides helpful error messages and safety features to make working with collections of data easier for new programmers.

The Array class is similar to a standard vector, but with additional safety features and simplified methods designed specifically for beginner programmers.

## Key Features

- **Range checking**: Prevents out-of-bounds errors with helpful messages
- **Simple syntax**: Easy-to-remember methods for common operations
- **Beginner-friendly**: Designed for students new to programming
- **Safe operations**: Clear error messages instead of mysterious crashes

## Getting Started

To use the `Array<>` class, include the appropriate header file:

```cpp
#include "array.h"
```

## Topics

- [Creating Arrays]({{ site.baseurl }}/cpp-intro/arrays/creating/)
- [Accessing Elements]({{ site.baseurl }}/cpp-intro/arrays/accessing/)
- [Modifying Arrays]({{ site.baseurl }}/cpp-intro/arrays/modifying/)
- [Using Loops with Arrays]({{ site.baseurl }}/cpp-intro/arrays/loops/)
- [Common Array Patterns]({{ site.baseurl }}/cpp-intro/arrays/patterns/)
"""
    create_file("docs/cpp-intro/arrays/index.md", array_index)
    
    # Create array documentation pages
    array_topics = {
        "creating": """---
layout: default
title: Creating Arrays
---

# Creating Arrays

An array is a collection of elements of the same type. Think of it like a numbered list or a row of storage boxes, where each item has its own position (index). Arrays are useful when you need to store multiple related values.

## Common Uses for Arrays

Arrays are perfect for storing:
- A list of student grades
- Coordinates for a game
- A collection of names
- Daily temperatures for a week

## Creating an Empty Array

To create an empty array, specify the type of elements it will contain:

```cpp
// Create an empty array of integers
Array<int> numbers;

// Create an empty array of strings
Array<string> names;

// Create an empty array of floating-point numbers
Array<double> prices;
```

## Creating an Array with Initial Values

You can create an array with values already in it using curly braces:

```cpp
// Create an array with some initial integer values
Array<int> scores = {95, 88, 76, 92, 85};

// Create an array of strings
Array<string> names = {"Alice", "Bob", "Charlie"};

// Create an array of doubles
Array<double> prices = {9.99, 14.50, 3.75};
```

## Choosing the Right Type

The type inside the angle brackets `<>` determines what kind of elements your array can hold:

- `Array<int>` can hold whole numbers (like 1, 42, -7)
- `Array<double>` can hold decimal numbers (like 3.14, -2.5)
- `Array<string>` can hold text
- `Array<bool>` can hold true/false values
- `Array<char>` can hold single characters

Remember that all elements in an array must be of the same type.
""",
        
        "accessing": """---
layout: default
title: Accessing Elements
---

# Accessing Elements

One of the most common operations is accessing individual elements of an array. The Array class provides safe and easy ways to work with the data it contains.

## Using the Square Bracket Operator `[]`

You can access individual elements in an array using square brackets `[]` with the index of the element you want.

**Important: Array indices start at 0, not 1!**

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Access the first element (index 0)
int firstScore = scores[0];  // 95

// Access the third element (index 2)
int thirdScore = scores[2];  // 76
```

## Modifying Elements

You can change the value of an element using the same square bracket notation:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Change the value of the second element (index 1)
scores[1] = 90;  // Changes 88 to 90

// Add 5 points to the fourth element (index 3)
scores[3] = scores[3] + 5;  // Changes 92 to 97
```

## Safety Features

One of the key benefits of the `Array<>` class is safety. If you try to access an element that doesn't exist, you'll get a helpful error message instead of a crash:

```cpp
Array<int> numbers = {10, 20, 30};

// This will throw an error with a message like:
// "Error: ArrayBase index 5 out of range (0, 2)"
int value = numbers[5];
```

This helps you quickly identify and fix index errors that would cause mysterious crashes with other array implementations.

## First and Last Elements

You can access the first element with `front()` and the last element with `back()`:

```cpp
Array<string> names = {"Alice", "Bob", "Charlie"};

string first = names.front();  // "Alice"
string last = names.back();    // "Charlie"
```

Like with the square bracket operator, the `front()` and `back()` methods will throw helpful error messages if the array is empty.
""",
        
        "modifying": """---
layout: default
title: Modifying Arrays
---

# Modifying Arrays

The Array class provides several methods for adding, removing, and changing elements.

## Adding Elements with `append`

The `append` method adds a new element to the end of the array:

```cpp
Array<string> fruits = {"apple", "banana"};

// Add a new element to the end
fruits.append("orange");  

// fruits now contains: {"apple", "banana", "orange"}
```

You can also use the alias `push_back` which does the same thing as `append`:

```cpp
fruits.push_back("grape");  // Same as append

// fruits now contains: {"apple", "banana", "orange", "grape"}
```

## Removing Elements with `removeAtIndex`

To remove an element at a specific position, use `removeAtIndex`:

```cpp
Array<string> colors = {"red", "green", "blue", "yellow"};

// Remove the element at index 1 (green)
colors.removeAtIndex(1);

// colors now contains: {"red", "blue", "yellow"}
```

When you remove an element, all elements after it will shift to fill the gap.

## Inserting Elements with `insertAtIndex`

To add an element at a specific position, use `insertAtIndex`:

```cpp
Array<string> weekdays = {"Monday", "Wednesday", "Thursday"};

// Insert "Tuesday" at index 1 (between Monday and Wednesday)
weekdays.insertAtIndex(1, "Tuesday");

// weekdays now contains: {"Monday", "Tuesday", "Wednesday", "Thursday"}
```

When you insert an element, all elements at or after that position will be shifted to make room.

## Changing the Size with `resize`

You can change the size of an array using the `resize` method:

```cpp
Array<int> numbers = {1, 2, 3};

// Resize to a larger size (new elements are initialized to 0)
numbers.resize(5);
// numbers now contains: {1, 2, 3, 0, 0}

// You can specify the value for new elements
Array<string> names = {"Alice", "Bob"};
names.resize(4, "Unknown");
// names now contains: {"Alice", "Bob", "Unknown", "Unknown"}

// Resize to a smaller size (extra elements are removed)
numbers.resize(2);
// numbers now contains: {1, 2}
```

## Clearing an Array with `clear`

To remove all elements from an array, use the `clear` method:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Remove all elements
scores.clear();

// scores is now empty, and scores.size() returns 0
```

## Getting the Size of an Array

The `size` method returns the number of elements in the array:

```cpp
Array<double> prices = {9.99, 15.50, 3.75, 20.00};

// Get the number of elements
int count = prices.size();  // 4

println("There are", count, "prices in the array.");
```

## Checking if an Array is Empty

You can check if an array has no elements using the `empty` method:

```cpp
Array<int> numbers;

if (numbers.empty()) {
    println("The array is empty!");
}

numbers.append(42);

if (!numbers.empty()) {
    println("The array now has elements!");
}
```
""",
        
        "loops": """---
layout: default
title: Using Loops with Arrays
---

# Using Loops with Arrays

Loops are especially useful for working with arrays, allowing you to process many elements with just a few lines of code. This page shows common patterns for using loops with arrays.

## Processing Each Element

The most common pattern is to use a for loop to process each element:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};
int sum = 0;

// Calculate the sum of all scores
for (int i = 0; i < scores.size(); i++) {
    sum += scores[i];
}

double average = static_cast<double>(sum) / scores.size();
println("Average score:", average);
```

## Finding Values in an Array

You can use a loop to search for specific values:

```cpp
Array<string> names = {"Alice", "Bob", "Charlie", "David"};
string searchName = "Charlie";
bool found = false;

for (int i = 0; i < names.size(); i++) {
    if (names[i] == searchName) {
        println("Found", searchName, "at position", i);
        found = true;
        break;  // Exit the loop once we've found what we're looking for
    }
}

if (!found) {
    println(searchName, "is not in the list.");
}
```

## Modifying All Elements

Loops make it easy to apply the same operation to every element:

```cpp
Array<int> prices = {100, 200, 300, 400};

// Apply a 10% discount to all prices
for (int i = 0; i < prices.size(); i++) {
    prices[i] = prices[i] * 0.9;  // Reduce each price by 10%
}

// Print the discounted prices
println("Discounted prices:");
for (int i = 0; i < prices.size(); i++) {
    println("Item", i, ":", prices[i]);
}
```

## Filtering Elements into a New Array

You can create a new array containing only elements that match certain criteria:

```cpp
Array<int> numbers = {15, 8, 42, 3, 29, 14, 7};
Array<int> evenNumbers;

// Create a new array with only the even numbers
for (int i = 0; i < numbers.size(); i++) {
    if (numbers[i] % 2 == 0) {  // Check if the number is even
        evenNumbers.append(numbers[i]);
    }
}

// Print the even numbers
println("Even numbers:");
for (int i = 0; i < evenNumbers.size(); i++) {
    println(evenNumbers[i]);
}
```

## Counting Occurrences

You can count how many times a specific value appears:

```cpp
Array<int> values = {4, 2, 7, 4, 8, 4, 1, 9, 4};
int count = 0;

// Count how many times 4 appears
for (int i = 0; i < values.size(); i++) {
    if (values[i] == 4) {
        count++;
    }
}

println("The value 4 appears", count, "times.");
```

## Finding the Maximum Value

You can find the largest value in an array:

```cpp
Array<int> temperatures = {72, 68, 73, 85, 79, 68};
int maxTemp = temperatures[0];  // Start with the first element

for (int i = 1; i < temperatures.size(); i++) {
    if (temperatures[i] > maxTemp) {
        maxTemp = temperatures[i];
    }
}

println("The highest temperature is", maxTemp);
```

## Reversing an Array

You can create a new array with elements in reverse order:

```cpp
Array<int> original = {1, 2, 3, 4, 5};
Array<int> reversed;

// Add elements in reverse order
for (int i = original.size() - 1; i >= 0; i--) {
    reversed.append(original[i]);
}

println("Original array:", original);
println("Reversed array:", reversed);
```
""",
        
        "patterns": """---
layout: default
title: Common Array Patterns
---

# Common Array Patterns

This page demonstrates common patterns and techniques for working with arrays that will help you solve many programming problems.

## Working with Multiple Arrays

Sometimes you need to use multiple arrays together:

```cpp
// Names and corresponding scores
Array<string> students = {"Alice", "Bob", "Charlie", "David"};
Array<int> scores = {92, 85, 78, 90};

// Find the student with the highest score
int highestIndex = 0;
for (int i = 1; i < scores.size(); i++) {
    if (scores[i] > scores[highestIndex]) {
        highestIndex = i;
    }
}

println("The student with the highest score is", students[highestIndex], 
        "with a score of", scores[highestIndex]);
```

## Building an Array Step by Step

Sometimes you need to build an array based on calculations:

```cpp
// Create an array of squares from 1 to 10
Array<int> squares;

for (int i = 1; i <= 10; i++) {
    squares.append(i * i);
}

// Print the squares
for (int i = 0; i < squares.size(); i++) {
    println(i+1, "squared =", squares[i]);
}
```

## Finding Elements that Match Criteria

When you need to locate elements based on conditions:

```cpp
Array<int> ages = {14, 7, 21, 16, 19, 8, 42, 17};
Array<int> adultIndices;

// Find indices of all adults (18 and older)
for (int i = 0; i < ages.size(); i++) {
    if (ages[i] >= 18) {
        adultIndices.append(i);
    }
}

println("Adult ages found at positions:");
for (int i = 0; i < adultIndices.size(); i++) {
    int index = adultIndices[i];
    println("Position", index, ":", ages[index]);
}
```

## Merging Arrays

You can combine multiple arrays:

```cpp
Array<string> list1 = {"apple", "banana", "cherry"};
Array<string> list2 = {"orange", "grape"};
Array<string> combined;

// Add all elements from the first list
for (int i = 0; i < list1.size(); i++) {
    combined.append(list1[i]);
}

// Add all elements from the second list
for (int i = 0; i < list2.size(); i++) {
    combined.append(list2[i]);
}

println("Combined list has", combined.size(), "elements");
```

## Checking if Arrays Are Equal

You can compare two arrays to see if they have the same elements:

```cpp
Array<int> array1 = {1, 2, 3, 4};
Array<int> array2 = {1, 2, 3, 4};
Array<int> array3 = {1, 2, 4, 3};

bool areEqual = true;

// First check if sizes match
if (array1.size() != array2.size()) {
    areEqual = false;
} else {
    // Then check each element
    for (int i = 0; i < array1.size(); i++) {
        if (array1[i] != array2[i]) {
            areEqual = false;
            break;
        }
    }
}

if (areEqual) {
    println("array1 and array2 are equal");
} else {
    println("array1 and array2 are NOT equal");
}
```

## Creating a Frequency Counter

Count how many times each value appears:

```cpp
Array<int> votes = {3, 1, 2, 3, 3, 1, 4, 2, 3, 2};
Array<int> candidates = {1, 2, 3, 4};
Array<int> counts = {0, 0, 0, 0};  // Initialize with zeros

// Count votes for each candidate
for (int i = 0; i < votes.size(); i++) {
    int candidate = votes[i];
    
    // Find the index of this candidate
    for (int j = 0; j < candidates.size(); j++) {
        if (candidates[j] == candidate) {
            counts[j]++;
            break;
        }
    }
}

// Display the results
for (int i = 0; i < candidates.size(); i++) {
    println("Candidate", candidates[i], "received", counts[i], "votes");
}
```

## Moving Elements Within an Array

Sometimes you need to rearrange elements:

```cpp
Array<string> queue = {"Alice", "Bob", "Charlie", "David"};

// Move the first person to the end of the queue
string firstPerson = queue[0];
queue.removeAtIndex(0);
queue.append(firstPerson);

println("After moving first person to the back:");
for (int i = 0; i < queue.size(); i++) {
    println(i, ":", queue[i]);
}
```
"""
    }
    
    # Create array documentation files
    for topic, content in array_topics.items():
        create_file(f"docs/cpp-intro/arrays/{topic}/index.md", content)
    
    # Create a CNAME file if needed
    # create_file("docs/CNAME", "yourdomain.com")
    
    # Create .nojekyll file if needed to prevent Jekyll processing
    # create_file("docs/.nojekyll", "")
    
    print("""
GitHub Pages repository has been successfully set up for 'Deploy from a branch'!

Next steps:
1. Commit and push these changes to your repository:
   git add .
   git commit -m "Set up GitHub Pages with Jekyll"
   git push

2. Configure GitHub Pages in your repository settings:
   - Go to Settings → Pages
   - Under "Build and deployment" → "Source", select "Deploy from a branch"
   - For "Branch", select "main" (or your default branch)
   - For the folder, select "/docs"
   - Click "Save"

3. Wait for GitHub to build your site (usually takes 1-2 minutes)
   Your site will be available at: https://mssmcs.github.io/programming/

This approach bypasses all the GitHub Actions complexities and uses GitHub's built-in 
Jekyll processing, which is more reliable for straightforward documentation sites.
""")

if __name__ == "__main__":
    setup_github_pages_repository()