# Python Extra (Built-In Functions)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------
# Introduction to Math Library

In Python, we have a function that calculate the product built-in to python.
See it all here : https://docs.python.org/3/library/functions.html

### Using abs()
```python
How to use
abs(<value>)

Example
abs(10) # Returns 10
abs(-10) # Returns 10
```
abs() is absolute in normal math way. It will not convert the variable to anything.

### Using chr()
```python
How to use
chr(<integer>)

Example
chr(65) # Returns 'A'
chr(97) # Returns 'a'
```
chr() converts number (integer only) to ASCII character.

### Using ord()
```python
How to use
ord(<character>)

Example
ord('A') # Returns 65
ord('a') # Returns 97
```
chr() converts single ASCII character to integer.

### Using len()
```python
How to use
len(<integer>)
len(<string>)

Example
len(10) # Equals to 0 to 9
len(1, 10) # Equals to 1 to 10

len("Happy") # Returns 5
len("A") # Returns 1
```
Mostly used with for loops. len is equal to length of something.

### Using max()
```python
How to use
max(arguments1, arguments2)

Example
max(1, 2) # Returns 2

a, b = 20, 10
max(a, b) # Returns 20
```

### Using min()
```python
How to use
min(arguments1, arguments2)

Example
min(1, 2) # Returns 1

a, b = 20, 10
min(a, b) # Returns 10
```

### Using pow()
```python
How to use
pow(<number>, <exponent power>, <modulo by>)

Example
pow(2, 3) # Returns 8
pow(2, 3, 2) # Returns 0
```

### Using round()
```python
How to use
round(<number>, significant number)

Example
round(12.1) # Returns 12
round(12.153, 2) # Returns 12.15
```
Python will round up / round down for you

If you want to forced round up / round down . You can use math library to help

### Using sorted()
```python
How to use
sorted(<lists of arrays>, reverse=False, key=none)

Example
text = [10,9,8,7,6,5,4,3,2,1]
sorted(text) # Returns [1,2,3,4,5,6,7,8,9,10]
```
Parameter reverse is when you want to sort in descending order

Parameter key is when you want to sort dictionary using only some data to determine

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
chr() convert value to string type (if possible)

float() convert value to float type (if possible)

int() convert value to integer type (if possible)
