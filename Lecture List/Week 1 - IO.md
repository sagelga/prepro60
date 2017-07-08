# Python Week 1 by P’ Kumamon (I/O)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------
# Types of Values
| **Integer** | **Float** | **String**   | **Boolean** |
| ----------- | --------- | ------------ | ----------- |
| int()       | float()   | str()        | bool()      |
| -1 0 1      | 1.1 3.555 | "Hello World"| True False  |

### Type of value check
```python
var = "Hello"
type(var) # Returns <class 'str'>

var = "1234"
type(var) # Returns <class 'str'>

var = 1234
type(var) # Returns <class 'int'>

var = 1234.56
type(var) # Returns <class 'float'>

var = True
type(var) # Returns <class 'bool'>
```

# Operators

### Basic Operator
| **Symbol**  | + | -    | *    | /   | //         | % | **   |
| ----------- | ----- | -------- | -------- | ------- | -------------- | ----- | -------- |
| **Name**    | Add   | Subtract | Multiply | Divide  | Floor Division | Mod   | Exponent |
| **Example** | 2+3   | 2-3      | 2*3      | 2/3     | 2//3           | 2&3   | 2**3     |
| **Results** | 5     | -1       | 6        | 0.66666 | 0              | 2     | 8        |

## Logic Operator
| **Type**    | **AND** | **OR** |
| ----------- | ------- | ------ |
| False False | False   | False  |
| False True  | False   | True   |
| True False  | False   | True   |
| True True   | True    | True   |

| **Type** | **NOT** |
| -------- | ----------- |
| False    | True        |
| True     | False       |

### Combined Operator

| **==**    | **!=**       | **<**     | **<=**                | **>**     | **>=**                |
| --------- | ------------ | --------- | --------------------- | --------- | --------------------- |
| Equals to | Not equal to | Less than | Less than or equal to | More than | More than or equal to |

| **Symbol**  | += | -=    | *=    | /=   | //=         | %= | **=   |
| ----------- | ----- | -------- | -------- | ------- | -------------- | ----- | -------- |
| **Name**    | Add (Increment)   | Subtract | Multiply | Divide  | Floor Division | Mod   | Exponent |
| **Example** | 2+3   | 2-3      | 2*3      | 2/3     | 2//3           | 2&3   | 2**3     |
| **Results** | 5     | -1       | 6        | 0.66666 | 0              | 2     | 8        |

In Python, there are no increment like ++ or -- like
```C
int num = 12;
num++

// num is equal to 13
```

so we use instead
```python
num = 12
num += 1

# num is equal to 13
```
## Order of Operations

Python is using PEMDAS rule. Do not use other mathematical rule to let Python compute
http://study.com/academy/lesson/what-is-pemdas-definition-rule-examples.html

| **P**           | **E**           | **M**              | **D**        | **A**        | **S**          |
| --------------- | --------------- | ------------------ | ------------ | ------------ | -------------- |
| **P**arenthesis | **E**xponential | **M**ultiplication | **D**ivision | **A**ddition | **S**utraction |
| ()              | **              | *                  | /            | +            | -              |

### String Operation
```python
text = "Hello"
text2 = "World"
print(text + text2) # Returns "HelloWorld"

text = "Hello"
text2 = "World"
print(text, text2) # Returns "Hello World"
```
### String with integer
```python
text = "Hello"
print(text * 5) # Returns "HelloHelloHelloHelloHello"

# This will not work!
text = "Hello"
text2 = "World"
print(text + text2 + 5) # Returns ERROR (You cannot add string with a integer type)

# so try to use this instead
text = "Hello"
text2 = "World"
print(text + text2 + str(5)) # Returns HelloWorld5
```

## Basic I/O

### print() Function
```python
text = "Hello"
print(text + "World") # Returns HelloWorld

text = 12
print(text, "World") # Returns 12 World

text = "Hello"
text2 = "World"
print(text + text2, sep=",") # Returns Hello,World

text = "Hello"
text2 = "World"
print(text + text2, end="!") # Returns HelloWorld!
```

### input() Function
```python
var_x = input() # var_x is now a string type.
var_x = int(input()) # Converts Float/Integer/String to Integer
var_x = float(input()) # Converts Float/Integer/String to Float
var_x = str(input()) # Converts Float/Integer/String to String
```

### Things getting complicated
```python
text = "Hello"
num = 1234

print(num+hello) # Returns error (string cannot be add with interger)

print(str(num)+text) # Returns 1234Hello (because they are in the same value type)
```

## Comments and DocString
```python
Use 3 " to make it as multiple line comments (DocString)

"""This is a docstring"""

Use '#' to make it as single line comment

# this is one line comment
```

## Minimum and Maximum
```python
How to use:
min(<argument 1>,<argument 2>)
Returns the lowest number

max(<argument 1>,<argument 2>)
Returns the highest number

# Using 2 arguments
var1 = 12
var2 = 21
return min(var1,var2)

# Using 3 arguments
var1 = 12
var2 = 21
var3 = 120
return min(min(var1,var2),var3)

# Using arguments from array
var = [12,24]
return min(var[0], var[1])
```

## Module Import

Always import the library as a global variable (before any functions)
It will reduce your time to import over and over again
```python
import math
def kumamon():
    print(math.pi())
kumamon()
```

## Library that you should know

### Basic Module List
https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20List/Python-Extra-Built-In-Functions.md

### Math Modules List
https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20List/Python-Extra-Math-Library.md
