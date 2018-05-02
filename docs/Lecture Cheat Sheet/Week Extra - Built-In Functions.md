# Built-In Functions

Copyright by P' Kumamon IT14. <br>
For education purpose only.

# Introduction to Built in Library
In Python, we have a function that calculate the product built-in to python. <br>
See it all here : https://docs.python.org/3/library/functions.html

### Using abs()
abs() is absolute in math language. Absoulte will returns a **positive** number from the value
```python
How to use
abs(<value>)

Example
abs(10)     # Returns 10
abs(-10)    # Returns 10
```

### Using chr()
chr() converts number (integer only) to ASCII character.
```python
How to use
chr(<integer>)

Example
chr(65) # Returns 'A'
chr(97) # Returns 'a'
```

### Using ord()
ord() converts single ASCII character to number (integer).
```python
How to use
ord(<character>)

Example
ord('A') # Returns 65
ord('a') # Returns 97
```

### Using len()
Mostly used with for loops. len is equal to length of something.
```python
How to use
len(<integer>)
len(<string>)
len(<array>)

Example
len(10)     # Equals to 0 to 9
len(1, 10)  # Equals to 1 to 10

len("Happy") # Returns 5
len("A") # Returns 1

len([1, 2, 3, 4, 5]) # Returns 5
```

### Using max()
Function will return the **largest** number from 2 arguments
```python
How to use
max(<arguments_1>, <arguments_2>)

Example
max(1, 2) # Returns 2

a, b = 20, 10
max(a, b) # Returns 20
```

### Using min()
Function will return the **smallest** number from 2 arguments
```python
How to use
min(<arguments_1>, <arguments_2>)

Example
min(1, 2) # Returns 1

a, b = 20, 10
min(a, b) # Returns 10
```

### Using pow()
Caculates a exponential values by using functions. This is absolutely optional way to calculate exponent
```python
How to use
pow(<number>, <exponent power>, <modulo by>)

Example
pow(2, 3) # Returns 8
pow(2, 3, 2) # Returns 0 (as 2**3 % 2)
```

### Using round()
Returns a number that will be rounded up (if >= .5) or round down (if < .5) <br>
If you want to forced round up or round down, You can use math library to help
```python
How to use
round(<number>, significant number)

Example
round(12.1) # Returns 12
round(12.153, 2) # Returns 12.15
```

### Using sorted()
Returns a arrays of values that have been sorted, pending on their value types <br>
Parameter reverse is when you want to sort in descending order <br>
Parameter key is when you want to sort dictionary using only some data to determine
```python
How to use
sorted(<lists of arrays>, reverse=False, key=none)

Example
text = [10,9,8,7,6,5,4,3,2,1]
sorted(text) # Returns [1,2,3,4,5,6,7,8,9,10]
```

### Using chr() float() int()
```python
chr(<value>)
float(<value>)
int(<value>)

Example
number = 12
chr(number) # Returns '12'

number = '12'
float(number) # Returns 12.0

number = 12.55
int(number) # Returns 12
```
chr() convert value to string type (if possible) <br>
float() convert value to float type (if possible) <br>
int() convert value to integer type (if possible)
