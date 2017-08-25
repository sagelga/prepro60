# Math Library

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

# Introduction to Math Library

In Python, we cannot calculate the complicate numbers by code, we use the function to make it easier to calculate everything. This will be the list of function that you should know before test!

Most of these functions are possible to be in any PSIT test. Some that are not listed are too complicate. But you can see it here : [https://docs.python.org/3.6/library/math.html](https://docs.python.org/3.6/library/math.html)

# Importing Library
Before using math library, you need to import it from the built-in library. If the library is imported, you can use their methods (function) inside that library
```python
import math
```

or

```python
import math as my_name_is_kumamon

# by using as command, the library name is changed to my_name_is_kumamon
my_name_is_kumamon.pi() # is equals to math.pi()
```

# Sample import on multiple functions
```python
import math # by importing here, all functions can use this library

def main(value, total):
  import os # by importing here, this function (main) can use this library
  print(value)
  print(total)
  x = math.fabs(calculate(value, total))
  print(x)

def calculate(value, total):
  return math.ceil(value / total)

main(12, 45)

# Using methods in library
Using the methods in library is easy is this. Program will find the absolute value (value is -2.55).
```python
import math

math.fabs(-2.55)
```

# Basic math functions
You should know how to use these before test. Everything is unexpected.

### Using absolute
or use exponent from built in function : abs()
Returns absolute x value
```python
math.fabs(x)
```

### Using exponent
or use exponent ** sign
Returns value as x^y
```python
math.pow(x, y)
```

### Using root
Returns value as x^1/2 (square root)
```python
math.sqrt(x)
```

### Using logarithms
Returns the value as log <base> <number>
```python
math.log(<number>, <base>)
```

### Using ceiling (round up)
Returns x as integer (rounding up)
```python
math.ceil(x)
```

### Using floor (round down)
Returns x as integer (rounding down)
```python
math.floor(x)
```

### Using factorial
Returns the value of the x!
```python
math.factorial(x)
```

### Using Pi (constant π)
Returns the value of pi (more accurate than 22/7, but not for 355/113)
```python
math.pi()
```

# Trigonometric Functions
| sin    | cos    | tan    |
| ------ | ------ | ------ |
| csc    | sec    | cot    |
| arcsin | arccos | arctan |

https://s-media-cache-ak0.pinimg.com/736x/9a/16/09/9a16096d6e68ee4f2b268b07c10111e6.jpg


### Using sin, cos, tan, csc, sec, cot, arcsin, arccos, arctan
```python
math.sin(<radians>)
math.cos(<radians>)
.
.
.
math.arctan(<radians>)
```

If the number is still a `degree`, you need to change it to `radians` by using

```python
math.radians(<degree>)

# Return radians value from the given <degree>
```
