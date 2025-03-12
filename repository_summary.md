# Repository Structure Overview

**Repository Root:** .

## Summary Statistics
- Total Directories: 10
- Total Files: 14

## File Type Breakdown
- .py: 1 files
- .md: 9 files
- .yml: 1 files
- .html: 3 files

## Directory Structure
- github-repo-explorer.py
- repository_summary.md
- docs
  - index.md
  - _config.yml
  - cpp-intro
    - index.md
    - arrays
      - index.md
      - accessing
        - index.md
      - creating
        - index.md
      - loops
        - index.md
      - modifying
        - index.md
      - patterns
        - index.md
  - _includes
    - auto-navigation.html
    - subtopics.html
  - _layouts
    - default.html

## Detailed File Types
- github-repo-explorer.py: .py
- repository_summary.md: .md
- index.md: .md
- _config.yml: .yml
- auto-navigation.html: .html
- subtopics.html: .html
- default.html: .html

## Index Files
### docs\index.md
**File Type:** .md

**Preview:**
```
---
layout: default
title: Docs
---

# Docs

Documentation and resources for docs.

## Topics

{% assign current_url = page.url %}
{% assign pages_list = site.pages | sort: "title" %}
{% assign has_children = false %}

<ul class="topic-list">
{% for node in pages_list %}
  {% assign node_url_parts = node.url | split: '/' %}
  {% assign node_url_parts_size = node_url_parts | size %}
  {% assign node_parent_path = node.url | split: '/' | pop | join: '/' | append: '/' %}
  
  {% if node_parent_path == current_url and node.url != current_url and node.title %}
    {% assign has_children = true %}
    <li>
      <a href="{{ site.baseurl }}{{ node.url }}">{{ node.title }}</a>
      {% if node.description %}
      <p class="topic-description">{{ node.description }}</p>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

{% if has_children == false %}
<p><em>No subtopics available yet.</em></p>
{% endif %}

<style>
  .topic-list {
    list-style-type: none;
    padding-left: 0;
  }
```

### docs\cpp-intro\index.md
**File Type:** .md

**Preview:**
```
---
layout: default
title: C++ Introduction
---

# C++ Introduction

An introduction to programming with C++.

## Topics

{% assign current_url = page.url %}
{% assign pages_list = site.pages | sort: "title" %}
{% assign has_children = false %}

<ul class="topic-list">
{% for node in pages_list %}
  {% assign node_url_parts = node.url | split: '/' %}
  {% assign node_url_parts_size = node_url_parts | size %}
  {% assign node_parent_path = node.url | split: '/' | pop | join: '/' | append: '/' %}
  
  {% if node_parent_path == current_url and node.url != current_url and node.title %}
    {% assign has_children = true %}
    <li>
      <a href="{{ site.baseurl }}{{ node.url }}">{{ node.title }}</a>
      {% if node.description %}
      <p class="topic-description">{{ node.description }}</p>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

{% if has_children == false %}
<p><em>No subtopics available yet.</em></p>
{% endif %}

<style>
  .topic-list {
    list-style-type: none;
```

### docs\cpp-intro\arrays\index.md
**File Type:** .md

**Preview:**
```
---
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

{% include subtopics.html %}
```

### docs\cpp-intro\arrays\accessing\index.md
**File Type:** .md

**Preview:**
```
---
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

## Safety Feat
```

### docs\cpp-intro\arrays\creating\index.md
**File Type:** .md

**Preview:**
```
---
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

// Create an array o
```

### docs\cpp-intro\arrays\loops\index.md
**File Type:** .md

**Preview:**
```
---
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
        break;
```

### docs\cpp-intro\arrays\modifying\index.md
**File Type:** .md

**Preview:**
```
---
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

When you remove an element, all elements after it will shift to fill the g
```

### docs\cpp-intro\arrays\patterns\index.md
**File Type:** .md

**Preview:**
```
---
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

// Print the squa
```

