# Python Week 5 by P’ Kumamon (Loops)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------
# Introduction to Loops
Q: Why do we need a loop?

A: It will simplify the use of coding and increse code quality

# Introduction to variable manipulator
### Using in
```python
How to use:
<text> in <text>

Example
"kumamon" in "kumamon is happy" # Returns True
"kumamoto" in "kumamon is happy" # Returns False
```
in is a tester that find the text within the text. Similarly to .find()

### Using range()
```python
How to use:
range(<stop>)
range(<start>, <stop>)

Example
range(10) -> 0,1,2,3,4,5,6,7,8,9
range(1,10) -> 1,2,3,4,5,6,7,8,9,10
```
range is a number array that continues the number as you like

# Introduction to For Loop
![](https://www.programtopia.net/sites/default/files/for_0.png)
```python
How to use:
for <variable> in range(<stop>):
for <variable> in range(<start>,<stop>):

Example
for i in range(10):
    print(i, end=" ")

# Returns 0 1 2 3 4 5 6 7 8 9
```
"for i" is to start a loop. 'i' variable will be number consists of "in range(x,y)".

### For loop without range()
```python
for i in "Kumamon":
    print(i, end=" ")

# Returns "K u m a m o n"
```
This loop will run for every character in "Kumamon". The loop will go for the length of that string

### For loop using text array
```python
text = "Kumamon"
for i in range(len(text)):
    print(i, end=" ")

# Returns "K u m a m o n"
```
Using range(len()) will help you to make you loop for a length of a string

### For loop using array
```python
text = [1,2,3,4,5]
for i in range(len(text)):
    print(i, end=" ")

# Returns "1 2 3 4 5"
```

### Nested For loops
![](http://etutorials.org/shared/images/tutorials/tutorial_23/09inf08.gif)
```python
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

# Returns
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
```

### Using For loops to call function
```python
def main():
    for i in range(2):
        for j in range(2):
            kumamon(i, j)

def kumamon(num1, num2):
    print(num1 + num2)

main()

# Returns
0
1
1
2
```

### Using for loops for n times
```python
for i in range(0,10):
    print(i, end=" ")

# Returns
0 1 2 3 4 5 6 7 8 9
```

### Applicate for loops with len()
```python
text = "1234567890"
for i in range(len(text)):
    print(i, end=" ")

# Returns
0 1 2 3 4 5 6 7 8 9
```

# Introduction to While Loop
![](http://pythonprogramminglanguage.com/wp-content/uploads/2015/11/while-loop.jpeg)
```python
How to use:
while <arguments>:
    # Will runs this when the argument is true

Example:
count = 10
while count > 5:
    print("Hello")
    count--
```

### Infinite Loop
![](http://3.bp.blogspot.com/_F7vpRIjAvYI/TIU7VpNlbzI/AAAAAAAABoI/s2clJ4LoWO0/s1600/image.png)
```python
while 1:
  print("This will go on and on forever....")

# Returns
This will go on and on forever....
This will go on and on forever....
This will go on and on forever....
...
...
...
# Programs will not end! Be aware!
```
### Work itself like FOR loops
```python
count = 10
while count != 0:
    print("Loop is now", count)
    count -= 1
```

# Loop types comparison
| Loop Type / Sample Environment | **For**      |**While**          |
| ------------------------------ | ------------ | ----------------- |
| Requires to start              | Length of loops| Argument that are true |
| Loop Control                   | Controllable (Using in range() or array)            | Controllable (Using break or making argument becomes false) |
| Stop when                      | Loop amount is done | When argument is false|
| Made for                       | Want exact number of loops    | Argument that can become false     |

# Using these to help
These can makes you get more of the loops.

### Using break()
```python
for i in range(10):
    print(i, end=" ")
    if i == 5:
        break

print("Loop is complete!")

# Returns
0 1 2 3 4 5 Loop is complete!
```
When the program runs to break argument, the loop will be cancelled

### Using continue()
```python
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")

print("Loop is complete!")

# Returns
0 1 2 3 4 6 7 8 9 Loop is complete!
```
When the program runs to continue argument, the loop will stop, and start from the beginning

| How to use   | **break**       | **continue**                 |
| ------------ | --------------- | ---------------------------- |
| **Benefits** | Stops the loop  | Reset the loop flow          |
| **For**      | Use as failsafe | Stop program from doing more |
