# Math Library

Copyright by P' Kumamon IT14. <br>
For education purpose only.

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
```

# Using methods in library
Using the methods in library is easy is this. Program will find the absolute value (value is -2.55).
```python
import math

math.fabs(-2.55)
```

# Basic math functions
You **should know how to use these** before test. Everything is unexpected.

### Using absolute
or use exponent from built in function : abs()
Returns absolute |x| value
```python
math.fabs(x)
```

### Using exponent
or use exponent \*\* sign
Returns value as x**y
```python
math.pow(<float or integer>, <exponent power>)
```

### Using root
Returns value as x^1/2 (square root)
```python
math.sqrt(<float or integer>)
```

### Using logarithms
Returns the value as log <base> <number>
```python
math.log(<number>, <base>)
```

or you may use
```python
math.log2(<number>)     # Set base = 2
math.log10(<number>)    # Set base = 10
```

### Using ceiling (round up)
Returns x as integer (rounding up)
```python
math.ceil(<float or integer>)
```

### Using floor (round down)
Returns x as integer (rounding down)
```python
math.floor(<float or integer>)
```

### Using factorial
Returns the value of the x!
```python
math.factorial(<integer>)
```

### Finding Greatest Commond Divisor (GCD)
Returns the GCD of integer A and B
```python
math.gcd(<integer_a>, <integer_a>)

```
### Using Pi (constant π)
Returns the value of pi (more accurate than 22/7, but not for 355/113)
```python
math.pi()
```

# Trigonometric Functions
| sin    | cos    | tan (sin/cos) |
| :----: | :----: | :-----------: |
| csc    | sec    | cot           |
| arcsin | arccos | arctan        |

![](https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fkisigcsemaths.files.wordpress.com%2F2014%2F01%2Ftrigratios.jpg&f=1)

### Using sin, cos, tan, csc, sec, cot, arcsin, arccos, arctan
```python
math.sin(<radians>)
math.cos(<radians>)
math.tan(<radians>)

math.csc(<radians>)
math.sec(<radians>)
math.cot(<radians>)

math.arcsin(<radians>)
math.arccos(<radians>)
math.arctan(<radians>)
```

If the number is still a `degree`, you need to change it to `radians` by using

```python
math.radians(<degree>)
```

If you already know some angle, and you want to find hypotenuse length, use
```python
math.hypot(<opposite/adjacent>, <opposite/adjacent>)
```
