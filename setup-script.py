#!/usr/bin/env python3
import os
import shutil
import sys

def create_directory(path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def write_file(path, content):
    """Write content to a file, creating parent directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def setup_repository(base_path):
    """Set up the repository structure with all necessary files."""
    
    # Create main directories
    create_directory(os.path.join(base_path, "docs"))
    create_directory(os.path.join(base_path, "docs", "cpp-intro"))
    create_directory(os.path.join(base_path, "docs", "cpp-intro", "arrays"))
    create_directory(os.path.join(base_path, ".github", "workflows"))
    
    # Create GitHub Actions workflow file
    github_actions_workflow = """name: Deploy Jekyll site to Pages

on:
  push:
    branches: ["main"]  # Adjust this to your default branch if different
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.2'
          bundler-cache: true
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Build with Jekyll
        run: bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: production
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: github-pages
          path: ./_site
          if-no-files-found: error

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
"""
    write_file(os.path.join(base_path, ".github", "workflows", "pages.yml"), github_actions_workflow)
    
    # Create Gemfile
    gemfile_content = """source "https://rubygems.org"

gem "jekyll", "~> 4.3.2"
gem "just-the-docs", "~> 0.5.3"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
"""
    write_file(os.path.join(base_path, "Gemfile"), gemfile_content)
    
    # Create _config.yml
    config_content = """title: "Computer Science Courses"
description: "Course materials for CS classes"
baseurl: "/programming"
url: "https://mssmcs.github.io"

# Build settings
theme: just-the-docs
color_scheme: light
search_enabled: true
heading_anchors: true

# Just the Docs settings
aux_links:
  "GitHub Repository":
    - "//github.com/mssmcs/programming"

# Default layout
defaults:
  -
    scope:
      path: ""
    values:
      layout: "default"
"""
    write_file(os.path.join(base_path, "docs", "_config.yml"), config_content)
    
    # Create main index file
    main_index_content = """---
layout: home
title: Home
nav_order: 1
---

# Computer Science Courses

Welcome to the course materials for CS classes.

## Available Resources

- [C++ Introduction](/programming/cpp-intro/)
  - [Array Class Documentation](/programming/cpp-intro/arrays/)
"""
    write_file(os.path.join(base_path, "docs", "index.md"), main_index_content)
    
    # Create cpp-intro index
    cpp_intro_index = """---
layout: default
title: C++ Introduction
nav_order: 2
has_children: true
permalink: /programming/cpp-intro/
---

# Introduction to C++

This section contains resources for learning C++ programming.

## Available Topics

- [Array Class](/programming/cpp-intro/arrays/)
"""
    write_file(os.path.join(base_path, "docs", "cpp-intro", "index.md"), cpp_intro_index)
    
    # Create array index page
    array_index = """---
layout: default
title: Array Class
parent: C++ Introduction
nav_order: 1
has_children: true
permalink: /programming/cpp-intro/arrays/
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

See the subpages for detailed information on creating and working with arrays.
"""
    write_file(os.path.join(base_path, "docs", "cpp-intro", "arrays", "index.md"), array_index)
    
    # Create array-creating.md
    array_creating = """---
layout: default
title: Creating Arrays
parent: Array Class
grand_parent: C++ Introduction
nav_order: 1
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
"""
    write_file(os.path.join(base_path, "docs", "cpp-intro", "arrays", "array-creating.md"), array_creating)
    
    # Create other array documentation files (similar pattern for each one)
    array_accessing = """---
layout: default
title: Accessing Elements
parent: Array Class
grand_parent: C++ Introduction
nav_order: 2
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
"""
    write_file(os.path.join(base_path, "docs", "cpp-intro", "arrays", "array-accessing.md"), array_accessing)
    
    # Add more array files as needed (array-modifying.md, array-loops.md, array-patterns.md)
    
    print("\nRepository setup complete!")
    print("Next steps:")
    print("1. Push these changes to your GitHub repository")
    print("2. Go to your repository settings -> Pages")
    print("3. Under 'Build and deployment', select 'GitHub Actions'")
    print("4. Wait for the GitHub Actions workflow to complete")
    print("5. Your site should be available at: https://mssmcs.github.io/programming/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.getcwd()
        print(f"No path specified, using current directory: {base_path}")
    
    setup_repository(base_path)
