# Python Tutorial
This is not a comprehensive Python tutorial but instead is intended to highlight the parts of the language that will be most important for us. You can download python form the [python.org](https://docs.python.org/3/library/index.html). I recommend installing Anaconda distribution, which already includes most of the libraries that are need to do data science.

### Keep in mind
 * Python is very slow when written badly.
 * Translate C code into Python is often bad idea.
 * Pythonic solution sometimes result in drastic performance improvement.
 * Utilize libraries' capabilities more than you skill.

### Tutorial Includes
 * Python Basic : Basic python syntax and concept
 * Python Advance : Object Oriented Programming
 * Numpy Basic : Simple Numpy Operation
 * Pandas Basic : Simple Pandas Operation
 * MatplotLib : Line, Point, Bar Graph, Pie Chart
 * Scikit Learn : (Will be added later)

### Libraries required
This tutorial is written in Python-3 (Numpy, Pandas, MatplotLib, Seaborn, Scikit-leanr). Anaconda already include all there libraries.

* To install anaconda click on [this link](https://www.anaconda.com/download/).

```sh
  $ source activate base

```


### Contribution
Happy to accept any pull requests if you want to add anything which can improve this tutorial.


# Python Core

## Comment


```python
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""
```




    'This type of comment is used to document the purpose of functions and classes.'



## Declaration/Initialization


```python
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
```

## Whitespace Formatting

Many languages use curly braces to delmit blocks of code. Python uses indentation(space and tab). This makes python code very readable, but it also means that you have to be very carefull with you formating:


```python
# Note that there is no bracket and semicolon ';'
# for i in [1,2,3,4,5]:
#     print(i+i)
```

## Arithmetic
Python 2.7 uses integer division by default, that is not what we want most of the time. Python 3.x uses normal division.


```python
# normal division
print(5/2)
# integer division
print(5//2)
```

    2.5
    2


## Strings

Strings can be delimited by single or double quotation marks (but the quotes have to match). Python used backslashes to encode special characters. You can use triple quotes to create multiline strings.


```python
single =   'string'
double =   "string"
triple = """string"""
```

## Loop


```python
# loop using 'in' keyword
for item in ('a','b','c','d'):
    print(item)

# traditional loop
start, end, calculate = 0 , 10 , 0
while (start < end):
    calculate += calculate
    start += 1
```

    a
    b
    c
    d


## Conditionals


```python
# conditional if - else ladder  
if False:
    print("Wrong Condition !")
elif False:
    print("Again Wrong Condition !")
else:
    print("Like Seriously !")
```

    Like Seriously !


## Data Types


```python
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None
```

## Function
A function is a rule for taking zero or more imputs and returning a corresponding output. To define function in python we use def. There is one special type of function in python known as lanbda function. More about lambda function [here](http://www.secnetix.de/olli/Python/lambda_functions.hawk).


```python
# function declaration/defination
def function_square(x):
    return(x*x)

# function calling
function_square(3)
```




    9




```python
# lambda function declaration/defination
function_lambda = lambda x: x**2

# function calling
function_lambda(3)
```




    9



## Exceptions

When something goes wrong,Python raises an exception. Unhandled, these will cause your program to crash. Exception can be handled using **try** and **except**.


```python
try:
    print(0/0)
except ZeroDivisionError:
    print("Divide by Zero")
```

    Divide by Zero


## Modules
Certain features of python are note loaded by default. These include both features included as part of the language as well as third-party features that yoy can download yourself. In order to use these features, you'll need to **import** the modules that contain them.


```python
import re # import the whole module
import re as regex # import the module as an alias
import matplotlib.pyplot as plt # import only some part of the module
from collections import defaultdict, Counter # import the specific feature or value from the module
```


```python
# never never do this
from re import * #  never do this
```


# Python Cheat Sheet

### Math
- abs() :	Returns absolute value of a number
- divmod() :	Returns quotient and remainder of integer division
- max() :	Returns the largest of the given arguments or items in an iterable
- min() :	Returns the smallest of the given arguments or items in an iterable
- pow() :	Raises a number to a power
- round() :	Rounds a floating-point value
- sum() :	Sums the items of an iterable

### Type Conversion
- ascii() :	Returns a string containing a printable representation of an object
- bin() :	Converts an integer to a binary string
- bool() :	Converts an argument to a Boolean value
- chr() :	Returns string representation of character given by integer argument
- complex() :	Returns a complex number constructed from arguments
- float() :	Returns a floating-point object constructed from a number or string
- hex() :	Converts an integer to a hexadecimal string
- int() :	Returns an integer object constructed from a number or string
- oct() :	Converts an integer to an octal string
- ord() :	Returns integer representation of a character
- repr() :	Returns a string containing a printable representation of an object
- str() :	Returns a string version of an object
- type() :	Returns the type of an object or creates a new type object

### Iterables and Iterators
- all() :	Returns True if all elements of an iterable are true
- any() :	Returns True if any elements of an iterable are true
- enumerate() :	Returns a list of tuples containing indices and values from an iterable
- filter() :	Filters elements from an iterable
- iter() :	Returns an iterator object
- len() :	Returns the length of an object
- map() :	Applies a function to every item of an iterable
- next() :	Retrieves the next item from an iterator
- range() :	Generates a range of integer values
- reversed() :	Returns a reverse iterator
- slice() :	Returns a slice object
- sorted() :	Returns a sorted list from an iterable
- zip() :	Creates an iterator that aggregates elements from iterables

### Composite Data Type
- bytearray() :	Creates and returns an object of the bytearray class
- bytes() :	Creates and returns a bytes object (similar to bytearray, but immutable)
- dict() :	Creates a dict object
- frozenset() :	Creates a frozenset object
- list() :	Constructs a list object
- object() :	Returns a new featureless object
- set() :	Creates a set object
- tuple() :	Creates a tuple object

### Classes, Attributes, and Inheritance
- classmethod() :	Returns a class method for a function
- delattr() :	Deletes an attribute from an object
- getattr() :	Returns the value of a named attribute of an object
- hasattr() :	Returns True if an object has a given attribute
- isinstance() :	Determines whether an object is an instance of a given class
- issubclass() :	Determines whether a class is a subclass of a given class
- property() :	Returns a property value of a class
- setattr() :	Sets the value of a named attribute of an object
- super() :	Returns a proxy object that delegates method calls to a parent or sibling class

### Input/Output
- format() :	Converts a value to a formatted representation
- input() :	Reads input from the console
- open() :	Opens a file and returns a file object
- print() :	Prints to a text stream or the console

### Variables, References, and Scope
- dir() :	Returns a list of names in current local scope or a list of object attributes
- globals() :	Returns a dictionary representing the current global symbol table
- id() :	Returns the identity of an object
- locals() :	Updates and returns a dictionary representing current local symbol table
- vars() :	Returns __dict__ attribute for a module, class, or object

### Miscellaneous
- callable() :	Returns True if object appears callable
- compile() :	Compiles source into a code or AST object
- eval() :	Evaluates a Python expression
- exec() :	Implements dynamic execution of Python code
- hash() :	Returns the hash value of an object
- help() :	Invokes the built-in help system
- memoryview() :	Returns a memory view object
- staticmethod() :	Returns a static method for a function
- __import__() :	Invoked by the import statement
