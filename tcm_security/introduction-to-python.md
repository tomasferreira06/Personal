# Introduction to Python

## Strings

### Creation

* Example: `my_string = 'Hello, World!'` or `my_string = "Hello, World!"`

### Accessing Characters

* You can access individual characters within a string using indexing, starting from 0.
* Example: `print(my_string[0])` would output 'H'.

### String Concatenation

* You can concatenate (join) two or more strings using the `+` operator.
* Example: `greeting = 'Hello' + ' ' + 'World!'` would result in 'Hello World!'.

### String Length

* The `len()` function can be used to determine the length (number of characters) of a string.
* Example: `print(len(my_string))` would output the length of the string.

### String Slicing

* You can extract a substring from a string using slicing, specifying the start and end indices.
* Example: `substring = my_string[7:12]` would extract the substring 'World'.

### String Methods

* Python provides various built-in methods to manipulate and transform strings.
* Examples include `upper()`, `lower()`, `strip()`, `split()`, `replace()`, and more.
* Example: `print(my_string.upper())` would output 'HELLO, WORLD!'.

### String Formatting

* String formatting allows you to embed values within a string. This can be done using the `%` operator , the `format()` method or an f string.
* Example:

```
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))
# Output: My name is Alice and I'm 30 years old.
print("My favorite movie is {}.".format(movie))
print(f"My favorite movie is {movie}."
```

## Math Functions in the `math` module

* `math.sqrt(x)`: Calculates the square root of `x`.
* `math.pow(x, y)`: Raises `x` to the power of `y`.
* `math.exp(x)`: Calculates the exponential value of `x` (e^x).
* `math.log(x)`: Calculates the natural logarithm of `x` (base e).
* `math.log10(x)`: Calculates the logarithm of `x` to base 10.
* `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Calculate the sine, cosine, and tangent of `x`, respectively (where `x` is in radians).
* `math.degrees(x)`: Converts `x` from radians to degrees.
* `math.radians(x)`: Converts `x` from degrees to radians.

### Math Operators

* Addition (`+`): Adds two numbers.
* Subtraction (\`\`): Subtracts one number from another.
* Multiplication (\`\`): Multiplies two numbers.
* Division (`/`): Divides one number by another.
* Integer Division (`//`): Performs division and returns the quotient as an integer (rounds down).
* Modulo (`%`): Returns the remainder of division.
* Exponentiation (`*`): Raises a number to a power.

#### Example usage:

```
import math
# Using math functions
print(math.sqrt(25)) # Output: 5.0
print(math.pow(2, 3)) # Output: 8.0
print(math.sin(math.pi/2)) # Output: 1.0

# Using math operators
x = 10 y = 3 print(x + y) # Output: 13
print(x / y) # Output: 3.3333333333333335
print(x // y) # Output: 3
print(x % y) # Output: 1
print(x ** y) # Output: 1000
```

### Relational Operators

Python provides several relational operators to compare values. Here are the commonly used relational operators:

* Equality (`==`): Checks if two values are equal.
* Inequality (`!=`): Checks if two values are not equal.
* Greater than (`>`): Checks if the left value is greater than the right value.
* Less than (`<`): Checks if the left value is less than the right value.
* Greater than or equal to (`>=`): Checks if the left value is greater than or equal to the right value.
* Less than or equal to (`<=`): Checks if the left value is less than or equal to the right value.

### Boolean Expressions

Boolean expressions are formed by combining relational expressions using logical operators. The logical operators in Python are:

* Logical AND (`and`): Returns `True` if both operands are `True`.
* Logical OR (`or`): Returns `True` if at least one operand is `True`.
* Logical NOT (`not`): Negates the value of the operand.

## List Creation

To create a list, you enclose comma-separated values within square brackets `[ ]`. Here's an example:

```
fruits = ["apple", "banana", "orange"]
```

### List Access

You can access individual elements in a list using indexing. Indexing starts from 0 for the first element and goes up to the length of the list minus one. Here are some examples:

```
print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"
```

### List Modification

Lists are mutable, which means you can modify their elements. You can assign new values to specific positions in the list or use methods to modify the list itself. Here are some examples:

```
fruits[1] = "grape"     # Modifying an element
fruits.append("kiwi")   # Adding an element to the end
fruits.remove("apple")  # Removing an element
```

### List Operations

Python provides various operations that can be performed on lists. Some common operations include:

* Concatenation: You can use the `+` operator to concatenate two or more lists.
* Length: The `len()` function returns the number of elements in a list.
* Slicing: You can extract a sublist from a list using slicing.
* Iteration: You can use a loop to iterate over the elements of a list.

#### Here are some examples:

```
fruits = ["apple", "banana", "orange"]
fruits2 = ["grape", "kiwi"]

combined = fruits + fruits2
print(combined)         # Output: ["apple", "banana", "orange", "grape", "kiwi"]

print(len(fruits))      # Output: 3

sublist = fruits[1:3]
print(sublist)          # Output: ["banana", "orange"]

for fruit in fruits:
    print(fruit)        # Output: "apple", "banana", "orange"
```

## Tuple Creation

To create a tuple, you enclose comma-separated values within parentheses `( )`. Here's an example:

```
fruits = ("apple", "banana", "orange")
```

### Tuple Access

You can access individual elements in a tuple using indexing, similar to lists. Indexing starts from 0 for the first element. Here are some examples:

```
print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"
```

### Tuple Immutability

Tuples are immutable, meaning you cannot modify their elements. Once a tuple is created, its values cannot be changed. For example, attempting to assign a new value to an element will result in an error. Here's an example:

```
fruits[1] = "grape"    # This will raise an error
```

### Tuple Operations

Although tuples are immutable, you can perform certain operations on them:

* Concatenation: You can use the `+` operator to concatenate two or more tuples.
* Length: The `len()` function returns the number of elements in a tuple.
* Slicing: You can extract a subtuple from a tuple using slicing.

#### Here are some examples:

```
fruits = ("apple", "banana", "orange")
fruits2 = ("grape", "kiwi")

combined = fruits + fruits2
print(combined)         # Output: ("apple", "banana", "orange", "grape", "kiwi")

print(len(fruits))      # Output: 3

subtuple = fruits[1:3]
print(subtuple)         # Output: ("banana", "orange")
```

## Loops

### for Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It executes a block of code a fixed number of times, based on the elements or items in the sequence. Here's the general syntax:

```
for item in sequence:
    # code to be executed for each item in the sequence
```

#### Example:

```
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

In this example, the `for` loop iterates over each item in the `fruits` list, and the block of code inside the loop (`print(fruit)`) is executed for each item. It will output:

```
apple
banana
orange
```

### while Loop

The `while` loop is used to repeatedly execute a block of code as long as a given condition is true. It continues looping until the condition becomes false. Here's the general syntax:

```
while condition:
    # code to be executed while the condition is true
```

Example:

```
count = 0
while count < 5:
    print(count)
    count += 1
```

In this example, the `while` loop will continue executing the code inside the loop (`print(count)`) as long as the condition `count < 5` is true. It will output:

```
0
1
2
3
4
```

### `break` and `continue` Statements

Within loops, you can use the `break` statement to exit the loop prematurely and the `continue` statement to skip the current iteration and move to the next one.

## Dictionaries

### Dictionary Creation

To create a dictionary, you enclose key-value pairs within curly braces `{ }`, separating each pair with a colon `:`. Here's an example:

```
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
```

### Dictionary Access

You can access the values in a dictionary by referring to their corresponding keys. Keys provide a way to uniquely identify and retrieve values. Here's an example:

```
print(student["name"])   # Output: "Alice"
print(student["age"])    # Output: 20
```

### Dictionary Modification

Dictionaries are mutable, which means you can modify their values by assigning new values to specific keys. Here's an example:

```
student["age"] = 21       # Modifying a value
student["city"] = "London"    # Adding a new key-value pair
```

### Dictionary Operations

Python provides various operations that can be performed on dictionaries. Some common operations include:

* Length: The `len()` function returns the number of key-value pairs in a dictionary.
* Iteration: You can iterate over the keys, values, or key-value pairs of a dictionary using loops.
* Deletion: You can remove a key-value pair from a dictionary using the `del` keyword.

#### Here are some examples:

```
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(len(student))          # Output: 3

for key in student:
    print(key, student[key])  # Output: "name Alice", "age 20", "major Computer Science"

del student["age"]           # Deleting a key-value pair
```

## Importing Modules

### Importing Entire Modules

To import an entire module, you use the `import` keyword followed by the module name. Here's an example:

```
import math

result = math.sqrt(25)
print(result)   # Output: 5.0
```

In this example, the `math` module is imported, and the `sqrt()` function from the module is used to calculate the square root of 25.

### Importing Specific Functions or Variables

If you only need to use specific functions or variables from a module, you can import them directly. Here's an example:

```
from math import sqrt

result = sqrt(25)
print(result)   # Output: 5.0
```

In this case, only the `sqrt()` function is imported from the `math` module, so you can use it directly without prefixing it with the module name.

### Importing Modules with an Alias

You can also import a module and give it an alias using the `as` keyword. This can be helpful when dealing with modules with long names or to avoid naming conflicts. Here's an example:

```
import math as m

result = m.sqrt(25)
print(result)   # Output: 5.0
```

In this example, the `math` module is imported and assigned the alias `m`, so you can use `m.sqrt()` instead of `math.sqrt()`.

### Importing All Functions and Variables

If you want to import all functions and variables from a module, you can use the \`\` wildcard character. However, it is generally recommended to import only what you need to avoid namespace pollution. Here's an example:

```
from math import *

result = sqrt(25)
print(result)   # Output: 5.0
```

In this case, all functions and variables from the `math` module are imported directly, allowing you to use them without prefixing with the module name.

## Sockets

### Socket Creation

To use sockets in Python, you need to import the `socket` module. You can create a socket object using the `socket.socket()` function, which takes two parameters: the address family (e.g., `socket.AF_INET` for IPv4) and the socket type (e.g., `socket.SOCK_STREAM` for TCP or `socket.SOCK_DGRAM` for UDP). Here's an example:

```
import socket

# Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### Socket Communication

Once you have a socket object, you can use various methods to establish connections, send data, and receive data. Here are some commonly used methods:

* `socket.connect(address)`: Establishes a connection to a remote address.
* `socket.bind(address)`: Binds the socket to a specific address and port.
* `socket.listen(backlog)`: Listens for incoming connections on a TCP socket.
* `socket.accept()`: Accepts an incoming connection and returns a new socket object for communication.
* `socket.send(data)`: Sends data over the socket.
* `socket.recv(buffer_size)`: Receives data from the socket.

#### Here's an example of a basic TCP server that listens for incoming connections:

```
import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    # Receive and send data
    data = client_socket.recv(1024)
    client_socket.send(b"Received: " + data)

    # Close the client socket
    client_socket.close()
```

## User Input

In Python, you can interact with the user and receive input using the `input()` function.

The `input()` function allows you to prompt the user for input and receive the input as a string.

#### Here's an explanation of user input in Python:

```
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

In this example, the `input()` function is used to prompt the user to enter their name.

The message "Enter your name: " is displayed to the user as a prompt.

The user can then type their name and press Enter.

The input provided by the user is stored in the variable `name`, and the program prints a greeting using the entered name.

The `input()` function always returns the user's input as a string.

If you need to convert the input to a different data type, such as an integer or float, you can use appropriate conversion functions like `int()` or `float()`.

```
age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer

print("You will be " + str(age + 1) + " next year.")
```

In this example, the user is asked to enter their age.

The input is stored as a string in the variable `age`.

To perform arithmetic calculations, the input is converted to an integer using the `int()` function.

The program then adds 1 to the age and prints the result.

## File Manipulation

### Reading Files

To read from a file, you need to open it in read mode using the `open()` function. Once the file is open, you can use methods like `read()`, `readline()`, or `readlines()` to retrieve the contents of the file.

* `read()`: Reads the entire content of the file as a string.
* `readline()`: Reads a single line from the file.
* `readlines()`: Reads all lines from the file and returns them as a list.

#### Here's an example of reading from a file:

```
# Open the file in read mode
file = open("example.txt", "r")

# Read the entire content
content = file.read()
print(content)

# Read a single line
line = file.readline()
print(line)

# Read all lines
lines = file.readlines()
print(lines)

# Close the file
file.close()
```

### Writing Files

To write to a file, you need to open it in write mode using the `open()` function. Once the file is open, you can use the `write()` method to write content to the file.

* `write(content)`: Writes the specified content to the file.

#### Here's an example of writing to a file:

```
# Open the file in write mode
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, World!\n")
file.write("This is a new line.")

# Close the file
file.close()
```

### Appending to Files

To append content to an existing file without overwriting its existing contents, you can open the file in append mode (`"a"`) using the `open()` function. Then, you can use the `write()` method to append content to the file.

```
# Open the file in append mode
file = open("example.txt", "a")

# Append content to the file
file.write("\nThis is appended content.")

# Close the file
file.close()
```

It is generally recommended to use the `with` statement when working with files. This ensures that the file is properly closed even if an exception occurs.

```
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Classes and Objects

### Classes

* A class is a blueprint or a template for creating objects.
* It defines the properties (attributes) and behaviors (methods) that objects of that class will possess.
* You can think of a class as a blueprint for creating instances of objects with similar characteristics and functionalities.

#### Here's an example of a simple class definition:

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

```

* In this example, the `Dog` class has attributes `name` and `age`, and methods `bark()` and `display_info()`.
* The `__init__()` method is a special method known as the constructor, which is called when an object of the class is created.

## Objects

* An object is an instance of a class.
* It is created based on the blueprint provided by the class.
* Each object has its own set of attributes and can invoke the methods defined in the class.
* You create objects by calling the class as if it were a function.

#### Here's an example:

```
# Create objects of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Call methods on the objects
dog1.bark()               # Output: "Woof!"
dog1.display_info()       # Output: "Name: Buddy", "Age: 5"

dog2.bark()               # Output: "Woof!"
dog2.display_info()       # Output: "Name: Max", "Age: 3"

```

In this example, `dog1` and `dog2` are objects created from the `Dog` class.

Each object has its own set of attributes (`name` and `age`) and can invoke the methods (`bark()` and `display_info()`) defined in the class.

Classes and objects are essential in object-oriented programming as they provide a way to organize code, encapsulate data, and define reusable entities.

They enable you to model real-world entities, create custom data types, and build complex systems by leveraging the principles of inheritance, polymorphism, and encapsulation.



























