# Python Tutorial
This is not a comprehensive [Python]((https://docs.python.org/3/library/index.html) tutorial but instead is intended to highlight the parts of the language that will be most important for getting started.

### Keep in mind
 * Python is very slow when written badly.
 * Translate C code into Python is often bad idea.
 * Pythonic solution sometimes result in drastic performance improvement.
 * Utilize librarie's capabilities more than you skill.

### How to get started?
 This tutorial is written in Python version 3. I recommend installing Anaconda distribution, which already includes most of the libraries that are required for this tutorials.

 **Installation:**
  1. Download [Anaconda](https://www.anaconda.com/download/) installer.
  2. Execute and complete the installer.
  3. Open [Anaconda Command Prompt]( ) and execute the code.
  ```sh
    $ source activate base
    $ jupyter notebook
  ```

**Get Code:**
 1. Create a [Github](https://github.com/join) account if you don't already have one.
 2. [Fork](https://help.github.com/articles/fork-a-repo/) the [learn-Python](https://github.com/llabhishekll/learn-Python) repository to your Github account.
 3. [Clone the forked repository](https://help.github.com/articles/cloning-a-repository/) on your local machine.


 ## Legends

 * :orange_book: — Jupyter Notebook
 * :newspaper: — Article/Blog/Document
 * :dvd: — Video Lecture

### Course Content

#### Module 1
- [ ] :orange_book: [Python Fundamental](https://github.com/llabhishekll/learn-Python/blob/master/00-Python-basic-syntax.ipynb)
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 2
- [ ] :orange_book: [Built in Function]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 3
- [ ] :orange_book: [String Manipulation]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 4
- [ ] :orange_book: [Python Data Structure]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 5
- [ ] :orange_book: [Class and Object]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 6
- [ ] :orange_book: [Iterators/Generators/Decorators]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 7
- [ ] :orange_book: [Python Comprehension]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 8
- [ ] :orange_book: [System/OS Module]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 9
- [ ] :orange_book: [File Handling]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 10
- [ ] :orange_book: [HTTP Requests]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 11
- [ ] :orange_book: [Web Scraping]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 12
- [ ] :orange_book: [CSV Module]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 13
- [ ] :orange_book: [Numpy Operation]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 14
- [ ] :orange_book: [Pandas Fundamental]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 15
- [ ] :orange_book: [Pandas Data Structure]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 16
- [ ] :orange_book: [Pandas Visualisation]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 17
- [ ] :orange_book: [MatplotLib Visualisation]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 18
- [ ] :orange_book: [Scikit Learn - Machine Learning ]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 19
- [ ] :orange_book: [Thread Subprocess]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 20
- [ ] :orange_book: [Python Miscellaneous]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 21
- [ ] :orange_book: [Python GUI]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 22
- [ ] :orange_book: [Python SQL]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 23
- [ ] :orange_book: [Error Handling]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 24
- [ ] :orange_book: [Python Application]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

#### Module 25
- [ ] :orange_book: [Python Code Profiling]()
- [ ] :newspaper: []()
- [ ] :dvd: []()

---

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

---

# Contribution
Happy to accept any pull requests if you want to add anything which can improve this tutorial.
