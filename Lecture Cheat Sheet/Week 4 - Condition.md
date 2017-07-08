# Python Week 4 by P’ Kumamon (Condition)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------
# Introduction to condition flow

Condition flow makes the program think out of decision. Some decision is harder to make or some decision is complicate, Python have covered you.

# What makes the argument true
|1|2|3|4|5|
|:-:|:-:|:-:|:-:|:-:|
|Equation is correct|Comparison of string is identical|Integer is not 0 (can be negative or positive)|Boolean is true|Logically true|

# How to compare strings
```python
var1 = "Hello"
var2 = "Hello"

return num1 == num2 # This line will return boolean of true. Because both string is identical
```

# If statement
### If statement will run when the argument is true.
```python
How to use:
if (<argument>):
  # This set of code will run when argument is true

Example:
kumamon = 12
if (kumamon > 10):
  print("Happy kumamon")

# Returns "Happy kumamon"
```

### When If statement will not work
```python
kumamon = 9

if (kumamon > 10):
  print("Heavy kumamon")

### Returns <none> (Because the statement is now false)
```

### Indentation on if statement
```python
kumamon = 9

if (kumamon = 9):
    print("Happy")
print("Kumamon")

# Returns "Happy Kumamon"
```

### If from variables
```python
kumamon = 1
if kumamon:
    print("Happy Kumamon")

# Returns "Happy Kumamon"

```python
kumamon = 10
if kumamon:
    print("Happy Kumamon")

# Returns "Happy Kumamon"

kumamon = -1
if kumamon:
    print("Happy Kumamon")

# Returns "Happy Kumamon"

kumamon = 0:
if kumamon:
    print("Happy Kumamon")

# Returns <none>
```

# If - Else statement

### Introduction to Else statement (Requires If statement)
```python
kumamon = 9
if kumamon > 10:
    print("Heavy kumamon")
else:
    print("Cute kumamon")

Returns:
"Cute kumamon"
```

### Bound of Else to If
```python
kumamon = 10
if kumamon == 10:
    print("Happy Happy kumamon")
if kumamon > 10:
    print("Heavy kumamon")
else:
    print("Cute kumamon")

Returns:
"Happy Happy kumamon"
"Cute kumamon"
```

### Else will not do when
```python
kumamon = 10
else:
    print("Happy Kumamon")

# Returns Syntax Error (as they have no bound to if statement)
```

# If - Elif statement

If and elif is used together to make more decision than just a plain if statement.

### Introduction to Elif
```python
kumamon = 10:
if kumamon == 11:
    print("Happy Kumamon")
elif kumamon == 10:
    print("Not Happy Kumamon")

# Returns "Not Happy Kumamon
```

### Elif = else if
```python
kumamon = 10:
if kumamon == 11:
    print("Happy Kumamon")
else:
  if kumamon == 10:
    print("Not Happy Kumamon")

# Returns "Not Happy Kumamon
```

# If - Elif - Else statement
You can pull the full power of Python by using these 3 statements

### Using in full potential
```python
kumamon = 11
if kumamon == 10:
  print("Happy Happy kumamon")
elif kumamon > 10:
  print("Heavy kumamon")
else: #This condition will run when kumamon < 10
  print("Cute kumamon")

Returns:
"Heavy kumamon"
```

# Nested control flow
Do anything you like, but beware of [too many branch](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20List/Week%20Extra%20-%20PyLint.md#11-too-many-branch)

### If Nested Flow
Try not to do this. As they are harder to debug.
```python
    if kumamon > 5:
      if kumamon > 4:
        if kumamon > 3:
          if kumamon > 2:
            if kumamon > 1:
              print("Happy Happy Kumamon 1")
            print("Happy Happy Kumamon 2")
          print("Happy Happy Kumamon 3")
        print("Happy Happy Kumamon 4")
      print("Happy Happy Kumamon 5")
```

### More nested flow
```python
    if kumamon == 10:
      print("Happy Happy kumamon")
      if kumamon == 10:
        print("Happy Happy kumamon")
        if kumamon == 10:
          print("Happy Happy kumamon")
        elif kumamon > 10:
          print("Heavy kumamon")
        else:
          print("Cute kumamon")
      elif kumamon > 10:
        print("Heavy kumamon")
      else:
        print("Cute kumamon")
    elif kumamon > 10:
      print("Heavy kumamon")
    else:
      print("Cute kumamon")
      if kumamon == 10:
        print("Happy Happy kumamon")
      elif kumamon > 10:
        print("Heavy kumamon")
      else:
        print("Cute kumamon")
```
