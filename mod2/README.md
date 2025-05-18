# PCEP-30-02 Module 2 Problem Bank

This module builds on Module 1 with 20 targeted exercises designed to strengthen specific areas identified in your feedback. Each question includes difficulty level, time estimates, scaffolding hints, and extension challenges to support your learning journey.

## How to Use This Module

- **Follow the Learning Paths**: Questions are organized into recommended sequences that build skills progressively
- **Use the Scaffolding**: Each question includes hints and step-by-step guidance if you get stuck
- **Challenge Yourself**: Try the extension challenges after completing the basic requirements
- **Track Your Progress**: Note your completion time and compare to the estimates
- **Reflect on Theory**: Pay attention to the theory components that explain key concepts

## Section 1 • Computer Programming & Python Fundamentals (4 Questions)

| # | Hands-on exercise (ready-to-run context) | Difficulty | Time Est. | PCEP link |
|---|------------------------------------------|------------|-----------|-----------|
| 1 | **Bitwise Flag Manipulation** – Start with `status_flags = 0b0000`. Write code to: 1) Set the 3rd bit (counting from right, 0-indexed), 2) Check if the 2nd bit is set, 3) Toggle the 1st bit, 4) Clear the 3rd bit. Print the binary representation after each operation.<br>**Hint**: Use the OR= operator to set a bit, AND with a mask to check, XOR= to toggle, and AND= with a negated mask to clear. | Basic | 5-7 min | §1.4 |
| 2 | **Number Base Converter** – Create a function that takes an integer and prints its representation in decimal, binary, octal, and hexadecimal. Test with: `num = 42`. Then create a second function that takes a string like "0b101010" or "0x2A" and converts it to decimal.<br>**Hint**: Use built-in functions `bin()`, `oct()`, `hex()` for the first part, and `int(s, 0)` can automatically detect the base from prefixes.<br>**Extension**: Add error handling for invalid inputs like "0b123" (invalid binary). | Intermediate | 8-10 min | §1.3, §1.4 |
| 3 | **Bitwise Shift Operations** – Start with `value = 21`. Use left and right shift operators to: 1) Double the value twice using left shifts, 2) Divide the original value by 4 using right shifts. Print the binary representation and decimal value after each operation.<br>**Theory**: In your comments, explain why shifting left by 1 doubles a number and why shifting right by 1 halves it (for positive integers). | Basic | 5-7 min | §1.4 |
| 4 | **Type Casting and Accuracy** – Create a script that demonstrates the limitations of floating-point accuracy. Start with `a = 0.1 + 0.2` and `b = 0.3`. Compare them with `==` and print the result. Then use `round()` to fix the comparison.<br>**Step-by-step**: 1) Print `a` and `b` with high precision using `{:.20f}` format, 2) Compare with `==`, 3) Use `round()` to fix, 4) Demonstrate type conversions with examples.<br>**Extension**: Implement a custom `almost_equal()` function that checks if two floats are within a small epsilon of each other. | Intermediate | 8-10 min | §1.4, §1.5 |

## Section 2 • Control Flow – Conditionals & Loops (6 Questions)

| # | Exercise (context baked in) | Difficulty | Time Est. | PCEP link |
|---|------------------------------|------------|-----------|-----------|
| 5 | **Nested Loop Pattern** – Create a simplified pyramid pattern first:<br>```<br>  *  <br> *** <br>*****<br>```<br>Then extend to a diamond pattern:<br>```<br>  *  <br> *** <br>*****<br> *** <br>  *  <br>```<br>**Scaffolding**: 1) First create the top half with two loops: outer for rows, inner for spaces and stars, 2) Then add the bottom half. | Intermediate | 10-12 min | §2.2 |
| 6 | **Loop with break and continue** – Given a list `numbers = [12, 15, 7, 3, 9, 20, 8, 14]`, use a loop with both `break` and `continue` to: 1) Skip even numbers, 2) Print odd numbers, 3) Stop when you find a number greater than 15.<br>**Hint**: Use `%` to check for even numbers, and an `if` with `continue`. Use another `if` with `break` for the stopping condition. | Basic | 5-7 min | §2.2 |
| 7 | **Input Validation with while-else** – Create a PIN validator that: 1) Asks for a 4-digit PIN, 2) Gives the user 3 attempts, 3) Uses a `while-else` construct to either grant access or lock the account after 3 failed attempts.<br>**Scaffolding**: Start with `attempts = 3` and `correct_pin = "1234"`. Use a `while attempts > 0:` loop and decrement `attempts` after each incorrect guess.<br>**Extension**: Add validation to ensure the input is exactly 4 digits. | Basic | 8-10 min | §2.2 |
| 8 | **For-Else Pattern** – Given a list of transactions `transactions = [125, 89, 234, 165, 42, 158, 325, 67]`, use a `for-else` construct to check if any transaction exceeds $300.<br>**Theory**: Explain in comments how the `for-else` construct differs from a regular `for` loop with a boolean flag.<br>**Extension**: Modify to find all transactions over $200 and print their indices. | Basic | 5-7 min | §2.2 |
| 9 | **Nested Conditional Logic** – Create a loan eligibility checker with nested if statements. Start with variables `credit_score = 720`, `income = 65000`, and `debt = 15000`.<br>**Scaffolding**: 1) First check credit score ranges, 2) Within each range, check income, 3) Finally check debt-to-income ratio.<br>**Refactoring challenge**: After implementing with nested ifs, refactor to use compound conditions with `and` to make the code more readable. | Intermediate | 8-10 min | §2.1 |
| 10 | **Loop with Counter Pattern** – Implement a password strength checker that loops through a password string and counts: lowercase letters, uppercase letters, digits, and special characters. Start with `password = "P@ssw0rd"`.<br>**Hint**: Use `isupper()`, `islower()`, `isdigit()` methods, and an `else` for special characters.<br>**Extension**: Add a minimum length requirement and give specific feedback on what's missing from weak passwords. | Intermediate | 8-10 min | §2.2 |

## Section 3 • Data Collections – Lists, Tuples, Dicts, Strings (4 Questions)

| # | Exercise (with sample structures) | Difficulty | Time Est. | PCEP link |
|---|-----------------------------------|------------|-----------|-----------|
| 11 | **Dictionary Comprehension** – Given two lists: `keys = ['name', 'age', 'job']` and `values = ['Alex', 28, 'Developer']`, create a dictionary using dictionary comprehension. Then, create a second dictionary that filters out any values that are not strings.<br>**Hint**: Use `zip(keys, values)` with a dictionary comprehension. For filtering, add an `if isinstance(v, str)` condition. | Basic | 5-7 min | §3.3 |
| 12 | **Nested Data Structures** – Work with this nested structure: `data = [{'name': 'Alice', 'scores': [85, 90, 92]}, {'name': 'Bob', 'scores': [70, 80, 75]}, {'name': 'Charlie', 'scores': [95, 85, 90]}]`.<br>**Step-by-step**: 1) Loop through the list, 2) For each dictionary, calculate the average of 'scores', 3) Add an 'average' key to each dictionary, 4) Sort the list by average score.<br>**Extension**: Add a function to find the student with the highest score in any single test. | Intermediate | 10-12 min | §3.1, §3.3 |
| 13 | **String Manipulation Challenge** – Given the string `text = "Python programming is both powerful and fun to learn!"`:<br>**Step-by-step**: 1) Create a dictionary to count vowels, 2) Replace spaces with hyphens, 3) Create a list of words longer than 5 characters, 4) Title-case each word.<br>**Extension**: Create a function that returns the most common consonant in the text. | Intermediate | 8-10 min | §3.4 |
| 14 | **List, Tuple, and Dictionary Conversion** – Start with a list of tuples representing students and scores: `data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]`.<br>**Scaffolding**: 1) Use a dictionary comprehension for list-to-dict conversion, 2) Use list comprehensions with indexing for tuple-to-lists, 3) Use a list comprehension with dictionary creation for list-to-dictionaries.<br>**Theory**: Comment on the mutability differences between these data structures and when you would choose each one. | Basic | 8-10 min | §3.1, §3.2, §3.3 |

## Section 4 • Functions & Exceptions (6 Questions)

| # | Exercise (sample calls included) | Difficulty | Time Est. | PCEP link |
|---|----------------------------------|------------|-----------|-----------|
| 15 | **Recursive Directory Tree** – Implement a recursive function `print_tree(level, max_depth)` that prints a directory-like tree structure using indentation.<br>**Scaffolding**: 1) Base case: if level == max_depth, print a file, 2) Recursive case: print a directory, then call the function for "contents" with level+1.<br>**Theory**: Explain in comments the two essential components of any recursive function. | Basic | 8-10 min | §4.1 |
| 16 | **Exception Hierarchy Practice** – Write a function `safe_divide(a, b)` that handles multiple exception types.<br>**Scaffolding**: 1) Start with a try block for the division, 2) Add except blocks in order from most specific to most general, 3) Include appropriate messages for each exception type.<br>**Extension**: Add a custom exception `NegativeDivisionError` that's raised if either number is negative. | Basic | 5-7 min | §4.3, §4.4 |
| 17 | **Function with Variable Arguments** – Create a function `stats(*args, option='all')` that calculates statistics on a variable number of inputs.<br>**Step-by-step**: 1) Check if args is empty and raise an exception if so, 2) Calculate min, max, sum, and average, 3) Return based on the option parameter.<br>**Extension**: Add support for a keyword argument `weights` that allows weighted averages. | Intermediate | 8-10 min | §4.2, §4.4 |
| 18 | **Recursive Fibonacci with Memoization** – First implement a basic recursive Fibonacci function. Then create an optimized version with memoization.<br>**Scaffolding**: 1) Basic version: if n <= 1 return n, else return fib(n-1) + fib(n-2), 2) Memoized version: check if n in memo, if so return it, otherwise calculate and store in memo.<br>**Theory**: Explain the time complexity difference between the two implementations. | Advanced | 10-12 min | §4.1, §4.4 |
| 19 | **Custom Exception Hierarchy** – Create a simplified version first: a single custom exception `BankingError` and a function that raises it. Then extend to a hierarchy.<br>**Step-by-step**: 1) Define `BankingError` class inheriting from `Exception`, 2) Define subclasses, 3) Implement the `withdraw()` function with appropriate exception raising.<br>**Extension**: Add a transaction log that records all successful withdrawals. | Advanced | 10-12 min | §4.3, §4.4 |
| 20 | **Function Scope and Closure** – Create a counter function that demonstrates closure.<br>**Theory**: First explain in comments what a closure is and why it's useful.<br>**Scaffolding**: 1) Define outer function with a local variable, 2) Define inner function that uses the outer function's variable, 3) Return the inner function, 4) Create two separate counters to demonstrate independence.<br>**Extension**: Modify to allow decrementing as well as incrementing. | Advanced | 8-10 min | §4.2 |

## Recommended Learning Paths

To maximize your learning, follow these suggested paths through the questions:

### Bitwise Operations Path
1. Start with Q1 (Bitwise Flag Manipulation) for basic operations
2. Move to Q3 (Bitwise Shift Operations) to understand shifts
3. Then try Q2 (Number Base Converter) to connect binary representation with different bases

### Control Flow Path
1. Begin with Q6 (Loop with break and continue) for basic loop control
2. Try Q8 (For-Else Pattern) to understand this Python-specific construct
3. Move to Q7 (Input Validation with while-else) for practical application
4. Then tackle Q10 (Loop with Counter Pattern) for multiple counters in a loop
5. Progress to Q9 (Nested Conditional Logic) for complex decision trees
6. Finally attempt Q5 (Nested Loop Pattern) for the most complex loop structure

### Data Collections Path
1. Start with Q14 (List, Tuple, and Dictionary Conversion) to understand the relationships
2. Try Q11 (Dictionary Comprehension) for compact dictionary creation
3. Move to Q13 (String Manipulation Challenge) for string operations
4. Finally tackle Q12 (Nested Data Structures) for working with complex data

### Functions and Exceptions Path
1. Begin with Q16 (Exception Hierarchy Practice) for basic exception handling
2. Try Q15 (Recursive Directory Tree) for simple recursion
3. Move to Q17 (Function with Variable Arguments) for function parameter flexibility
4. Progress to Q19 (Custom Exception Hierarchy) for creating your own exceptions
5. Try Q18 (Recursive Fibonacci with Memoization) for optimized recursion
6. Finally tackle Q20 (Function Scope and Closure) for advanced function concepts

## How to drill efficiently ✔️

* Copy the "context" snippet into a fresh file, then code the logic underneath
* Comment the top line of each script with its syllabus reference, e.g., `# PCEP §3.1 – lists / slicing / len()`
* Time yourself—compare your time to the estimates provided
* Use the hints only if you get stuck for more than 2-3 minutes
* After completing the basic task, try the extension challenge
* Review the theory components to deepen your understanding
* Follow the learning paths for a structured approach to building skills

This module is designed to strengthen your weaker areas while building on your existing knowledge. Focus particularly on the Control Flow and Functions & Exceptions sections, which were identified as areas for improvement in your Module 1 feedback.

Happy coding, and may your PCEP preparation continue to strengthen! 🚀
