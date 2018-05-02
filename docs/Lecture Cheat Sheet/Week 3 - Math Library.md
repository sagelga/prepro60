# Math Library
In Python, we cannot calculate the complicate numbers by code, we use the function to make it easier to calculate everything. This will be the list of function that you should know before test!

Most of these functions are possible to be in any PSIT test. Some that are not listed are too complicate. But you can see it [here](https://docs.python.org/3.6/library/math.html)

## Importing Library
Before using math library, you need to import it from the built-in library. If the library is imported, you can use their methods (function) inside that library

```python
import math
```

or

```python
import math as new_package_name
```
with that, you can call `new_package_name.pi()` equivalent to `math.pi()`

## Sample import on multiple functions
```python
import math

def main(value, total):
import os
print(value)
print(total)
x = math.fabs(calculate(value, total))
print(x)

def calculate(value, total):
return math.ceil(value / total)

main(12, 45)
```
by putting a `import math` outside the function makes it a global type of package.

## Using methods in library
Using the methods in library is easy is this. Program will find the absolute value (value is -2.55).
```python
import math
math.fabs(-2.55)
```

## Basic math functions
These are just a few elements in math function. There will be a help in Think Python book.

### Absolute Values
Make the integer or float becomes positive only.
```python
math.fabs([value])
```
or use built-in function `abs()` instead.

### Using exponent
or use exponent \*\* sign
Returns value as x**y
```python
math.pow([value], [exponent power])
```

### Using root
Returns value as x^1/2 (square root)
```python
math.sqrt([float or integer])
```

### Using logarithms
Returns the value as log [base] [number]
```python
math.log([number], [base])
```

or use a predefined log level

```python
math.log2([number])
math.log10([number])
```

### Using ceiling (round up)
Returns value as integer (rounding up)
```python
math.ceil([float or integer])
```

### Using floor (round down)
Returns value as integer (rounding down)
```python
math.floor([float or integer])
```

### Using factorial
Returns the value of the value factorial
```python
math.factorial([integer])
```

### Finding Greatest Common Divisor (GCD)
Returns the GCD of integer A and B
```python
math.gcd([integer_a], [integer_a])

```
### Using constant Pi value (π)
Returns the value of pi (more accurate than 22/7, but not for 355/113)
```python
math.pi()
```

## Trigonometric Functions
![](https://engineering.purdue.edu/~asm215/topics/trigfunc.gif)

```python
math.sin([radians])
math.cos([radians])
math.tan([radians])

math.csc([radians])
math.sec([radians])
math.cot([radians])

math.arcsin([radians])
math.arccos([radians])
math.arctan([radians])
```

If the number is still a `degree`, you need to change it to `radians` by using

```python
math.radians([degree])
```

If you already know some angle, and you want to find hypotenuse length, use
```python
math.hypot([opposite/adjacent], [opposite/adjacent])
```
