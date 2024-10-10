from fpdf import FPDF

# Create a PDF document for Unit 1
pdf_unit1 = FPDF()
pdf_unit1.set_auto_page_break(auto=True, margin=15)
pdf_unit1.add_page()

# Title for Unit 1
pdf_unit1.set_font("Arial", 'B', 16)
pdf_unit1.cell(0, 10, 'Python Programming - Unit 1', ln=True, align='C')

# Adding Unit 1 Questions and Answers
unit_1_content = [
    ("1. What is Python? List and explain features of Python.",
     "Python is a high-level, interpreted, and general-purpose programming language. "
     "It was created by Guido van Rossum and first released in 1991. Python is known for its simplicity, readability, and ease of use. "
     "It supports multiple programming paradigms, such as procedural, object-oriented, and functional programming.\n\n"
     "Features of Python include:\n"
     "1. Easy to learn and use: Python has a simple syntax, which makes it easy for beginners.\n"
     "2. Interpreted language: Python code is executed line by line, which makes debugging easier.\n"
     "3. Cross-platform: Python can run on various platforms such as Windows, Mac, Linux, etc.\n"
     "4. Large standard library: Python comes with a vast standard library, providing many pre-built functions.\n"
     "5. Open-source: Python is open-source and has a large community for support.\n"
     "6. Dynamic typing: Python allows dynamic typing, meaning variables can change types dynamically during execution."),
    
    ("2. Explain if…else statement with example.",
     "The if…else statement in Python is used for conditional execution. It allows a program to perform one action if a condition is true, "
     "and a different action if the condition is false.\n\n"
     "Example:\n"
     "```python\n"
     "x = 10\n"
     "if x > 5:\n"
     "    print('x is greater than 5')\n"
     "else:\n"
     "    print('x is less than or equal to 5')\n"
     "```"),
    
    ("3. Write a program to print numbers from 100 to 1.",
     "```python\n"
     "for i in range(100, 0, -1):\n"
     "    print(i)\n"
     "```"),

    ("4. Explain while loop in Python with example.",
     "A while loop in Python repeatedly executes a block of code as long as the specified condition is true.\n\n"
     "Example:\n"
     "```python\n"
     "x = 5\n"
     "while x > 0:\n"
     "    print(x)\n"
     "    x -= 1\n"
     "```"),

    ("5. Write a Python program to get a number and check whether it is odd or even.",
     "```python\n"
     "num = int(input('Enter a number: '))\n"
     "if num % 2 == 0:\n"
     "    print(f'{num} is even')\n"
     "else:\n"
     "    print(f'{num} is odd')\n"
     "```"),

    ("6. Explain membership, identity, and relation operators in Python with examples.",
     "1. Membership operators: These are used to check if a value is a member of a sequence like a string, list, or tuple.\n\n"
     "- `in`: Returns `True` if the value is found in the sequence.\n"
     "- `not in`: Returns `True` if the value is not found in the sequence.\n\n"
     "Example:\n"
     "```python\n"
     "x = 'Python'\n"
     "print('P' in x)  # True\n"
     "print('p' not in x)  # True\n"
     "```\n\n"
     "2. Identity operators: These check if two values refer to the same object in memory.\n\n"
     "- `is`: Returns `True` if two variables point to the same object.\n"
     "- `is not`: Returns `True` if two variables do not point to the same object.\n\n"
     "Example:\n"
     "```python\n"
     "x = [1, 2, 3]\n"
     "y = x\n"
     "print(x is y)  # True\n"
     "```\n\n"
     "3. Relational operators: These compare the values of two operands and determine the relationship between them.\n\n"
     "- `>` (greater than), `<` (less than), `==` (equal to), `!=` (not equal to)\n\n"
     "Example:\n"
     "```python\n"
     "a = 10\n"
     "b = 20\n"
     "print(a > b)  # False\n"
     "print(a != b)  # True\n"
     "```"),
    
    ("7. How to achieve type conversion in Python? Explain with example.",
     "Type conversion in Python refers to converting a value from one data type to another. "
     "It can be achieved using built-in functions like `int()`, `float()`, `str()`, and more.\n\n"
     "Example:\n"
     "```python\n"
     "a = 5  # int\n"
     "b = float(a)  # convert int to float\n"
     "print(a)  # 5\n"
     "print(b)  # 5.0\n"
     "```"),
    
    ("8. What is debugging? Explain the types of errors.",
     "Debugging is the process of finding and fixing errors in a program.\n\n"
     "There are three types of errors in Python:\n"
     "1. Syntax Errors: These occur when the Python interpreter finds a line that violates Python’s grammar rules.\n"
     "2. Runtime Errors: These occur while the program is running, often caused by operations like dividing by zero or using an undefined variable.\n"
     "3. Logical Errors: These occur when the program runs without crashing but produces incorrect results due to flaws in the logic."),

    ("9. Write a program to get a number and check positive or negative.",
     "```python\n"
     "num = int(input('Enter a number: '))\n"
     "if num > 0:\n"
     "    print(f'{num} is positive')\n"
     "elif num < 0:\n"
     "    print(f'{num} is negative')\n"
     "else:\n"
     "    print('The number is zero')\n"
     "```"),

    ("10. Explain the various brackets used in Python.",
     "In Python, the following types of brackets are used:\n\n"
     "1. Parentheses `()`: Used in function calls and defining tuples.\n"
     "2. Square brackets `[]`: Used for indexing, slicing, and defining lists.\n"
     "3. Curly brackets `{}`: Used for defining dictionaries and sets.\n"
     "Example:\n"
     "```python\n"
     "list1 = [1, 2, 3]  # Square brackets for list\n"
     "tuple1 = (1, 2, 3)  # Parentheses for tuple\n"
     "dict1 = {1: 'a', 2: 'b'}  # Curly brackets for dictionary\n"
     "```"),
]

# Adding Unit 1 content to PDF
for title, content in unit_1_content:
    pdf_unit1.set_font("Arial", 'B', 12)
    pdf_unit1.multi_cell(0, 10, title)
    pdf_unit1.set_font("Arial", '', 12)
    pdf_unit1.multi_cell(0, 10, content)
    pdf_unit1.cell(0, 10, '', ln=True)  # Add a line break

# Save the PDF for Unit 1
unit1_pdf_path = '/mnt/data/Python_Programming_Unit_1.pdf'
pdf_unit1.output(unit1_pdf_path)

unit1_pdf_path
