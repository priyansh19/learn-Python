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
