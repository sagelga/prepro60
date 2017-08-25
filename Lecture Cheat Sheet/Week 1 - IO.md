# Input and Output

## Lecture List

|Week 1|Week 2|Week 3|Week 4|Week 5|Week 6|Week 7|Week 8|Week 9|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|[Click](/Lecture%20Cheat%20Sheet/Week1%20-%20IO.md)|[Click](/Lecture%20Cheat%20Sheet/Week%202%20-%20Functions.md)|[Click](/Lecture%20Cheat%20Sheet/Week%203%20-%20Math%20Library.md%20)|[Click](/Lecture%20Cheat%20Sheet/Week%204%20-%20Strings.md)|[Click](/Lecture%20Cheat%20Sheet/Week%205%20-%20Condition.md%20)|[Click](/Lecture%20Cheat%20Sheet/Week%206%20-%20Loops.md)|[Click](/Lecture%20Cheat%20Sheet/Week%207%20-%20Lists%20+%20Tuples.md)|[Click](/Lecture%20Cheat%20Sheet/Week%208%20-%20Dictionary.md)|[Click](/Lecture%20Cheat%20Sheet/Week%209%20-%20Recursion.md)|

## Follow me on GitHub
|<a href="https://github.com/sagelga"><img src="https://avatars0.githubusercontent.com/u/13056824" width="100px"></a>  |
|:-:|  
|@sagelga|

Copyright by P' Kumamon IT14. <br>
For education purpose only.

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)

----------

# Basic types of values
| **Integer** | **Float** | **String**   | **Boolean** |
| ----------- | --------- | ------------ | ----------- |
| int()       | float()   | str()        | bool()      |
| -1 0 1      | 1.1 3.555 | "Hello World"| True False  |

### Checking value type
Python has a built-in function to let you know what the current variable holds what type of variable

By using
```python
type(<variable or values>)
```

as example of
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

# More type of variable
There is a few more thing that you need to know. <br>
By the computer code, every value is stored in a memory slot. Set of memory address is called **array**. <br>
This means, every variable can be stored in array, even array itself. <br>
To learn more, please go to lists + tuple lecture.

# Operators
Operator allows you to calculate arithmetic problems. <br>
But in the case of computer arithmetic problem, it is far more harder and more complex than you imagine. <br>
This is a lists of operators that you use to calculate problems.

### Basic Operator
| **Symbol**  | +     | -        | *        | /       | //             | %       | **       |
| ----------- | ----- | -------- | -------- | ------- | -------------- | ------- | -------- |
| **Name**    | Add   | Subtract | Multiply | Divide  | Floor Division | Modulus | Exponent |
| **Example** | 2+3   | 2-3      | 2*3      | 2/3     | 2//3           | 2&3     | 2**3     |
| **Results** | 5     | -1       | 6        | 0.66666 | 0              | 2       | 8        |

```python
value_a = 2
value_b = 3

return value_a + value_b    # Returns 5
return value_a - value_b    # Returns -1
return value_a * value_b    # Returns 6
return value_a / value_b    # Returns 0.666666 (or it can go weird)
return value_a // value_b   # Returns 0
return value_a % value_b    # Returns 2
return value_a ** value_b   # Returns 8

```

## Logic Operator
| **Type**    | **and** | **or** |
| ----------- | ------- | ------ |
| False False | False   | False  |
| False True  | False   | True   |
| True False  | False   | True   |
| True True   | True    | True   |

```python
return False and False  # Return False
return False and True   # Return False
return True and False   # Return False
return True and True    # Return True

return False or False  # Return False
return False or True   # Return True
return True or False   # Return True
return True or True    # Return True
```

| **Type** | **not** |
| -------- | ----------- |
| False    | True        |
| True     | False       |

```python
return not False # Return True
return not True # Return False
```

### Combined Operator

| **==**    | **!=**       | **<**     | **<=**                | **>**     | **>=**                |
| --------- | ------------ | --------- | --------------------- | --------- | --------------------- |
| Equals to | Not equal to | Less than | Less than or equal to | More than | More than or equal to |

| **Symbol**  | +=    | -=       | *=       | /=      | //=            | %=  | **=      |
| ----------- | ----- | -------- | -------- | ------- | -------------- | --- | -------- |
| **Name**    | Add   | Subtract | Multiply | Divide  | Floor Division | Mod | Exponent |
| **Example** | 2+3   | 2-3      | 2*3      | 2/3     | 2//3           | 2&3 | 2**3     |
| **Results** | 5     | -1       | 6        | 0.66666 | 0              | 2   | 8        |

In Python, there are no increment like ++ or -- like
```C
// Written in C language

int num = 12;
num++

// num is equal to 13
```

so we use the old way
```python
# Written in Python language

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

For more precise calculations, use parenthesis as much as you can

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

print(num+hello) # Returns error (string cannot be add with integer)

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
- Basic Module List
- Math Modules List
