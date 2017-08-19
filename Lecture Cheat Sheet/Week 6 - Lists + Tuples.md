# Python Week 6 by P’ Kumamon (Lists + Tuples)

## Lecture List

|Week 1|Week 2|Week 3|Week 4|Week 5|Week 6|Week 7|Week 8|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%201%20-%20IO.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%202%20-%20Functions.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%203%20-%20Strings.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%204%20-%20Condition.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%205%20-%20Loops.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%206%20-%20Lists%20%2B%20Tuples.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%207%20-%20Dictionary.md)|[Click](https://github.com/sagelga/PreProgramming-60/blob/master/Lecture%20Cheat%20Sheet/Week%208%20-%20Recursion.md)|

## Follow me on GitHub
<a href="https://github.com/sagelga"><img src="https://avatars0.githubusercontent.com/u/13056824" width="100px"></a>    
### @sagelga

Copyright by P' Kumamon IT14.
For education purpose only

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)

----------

# Introduction to Arrays
Array is a set of related data. In Python we have two difference types of array called List and Tuples.

# Introduction to Lists
Like a string, a list is a sequence of values. In string, the value are characters; in a list, they can be any type. The values in a list are called **elements** or sometimes **items**.

There are several ways to create a new list; the simplest is enclose the elements in square brackets ([ and ])

### Create an array
```python
kumamon = ['Kumamon', 'is', 'so', 'cute']
numbers = [1, 2, 3, 4]
blank = []
initiate = list()
```

as visualized from kumamon

| **Value**          | Kumamon | is | so | cute |
| ------------------ | ------- | -- | -- | ---- |
| **Array Number**   | 0       | 1  | 2  | 3    |
| **Logical Number** | 1       | 2  | 3  | 4    |


then looked at numbers

| **Value**          | 1 | 2 | 3 | 4 |
| ------------------ | - | - | - | - |
| **Array Number**   | 0 | 1 | 2 | 3 |
| **Logical Number** | 1 | 2 | 3 | 4 |

# Adding More Elements to array
### Using .append()
```Python
kumamon = [1,2,3,4]
kumamon.append(5)

# kumamon now equals to
[1, 2, 3, 4, 5]
```

### Using .split()
```Python
How to use:
<variable name>.split("<separator you are using>")


text = "I am a happy Kumamon"
return text.split() # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']

text = "I,am,a,happy,Kumamon"
return text.split(",") # Returns array ['I', 'am', 'a', 'happy', 'Kumamon']
```

### Add from other array
```python
text1 = ["Happy"]
text2 = ["Kumamon"]
return text1+text2

# Returns
["Happy", "Kumamon"]
```

# Modifying Elements in Array
### Using .sort() or sorted()
```python
kumamon = [1, 3, 4, 2, 5]
kumamon.sort()
# or sorted(kumamon)

# kumamon now equals to
[1, 2, 3, 4, 5]
```

### Using reverse sorting
```Python
kumamon = [1, 3, 4, 2, 5]
kumamon.sort(reverse = True)

# kumamon now equals to
[5, 4, 3, 2, 1]
```

### Sort is from ASCII
Sort will find the character that has the lowest ASCII values (if assigned with string values)
```Python
kumamon = ['9', '1', 'a', 'A']
kumamon = kumamon.sort()

# kumamon now equals to
['1', '9', 'A', 'a']
```

Again, sorting use the comparing techniques, so integer cannot be sorted with strings
```Python
kumamon = [9, 1, 'a', 'A']
kumamon = kumamon.sort()

# Return ValueError because integer cannot be compared with character
```

# Using Elements in Array
### Using .pop()
.pop() will return that value and then remove that item
```Python
"""
How to use:
<variable name>.pop("<character/text/array number you want to use>")
-> Returns the selected item, and removing them from array
"""

kumamon = ["Happy", "Funny", "Fat"]
print(kumamon.pop(1))

# Returns "Funny"
# and kumamon = ["Happy", "Fat"]
```

# Remove Elements in Array
### Using .remove()
.remove() will remove that element from the array
```python
"""
How to use:
<variable name>.remove("<character/text/array number you want to remove>")
-> Variable will update as you wish
"""

kumamon = ["Happy", "Funny", "Fat"]
kumamon.remove("Funny")

# kumamon is now equals to ["Happy", "Fat"]
```

## Using .strip()
```Python
"""
How to use:
<variable name>.strip("<character/text you want to remove>")
-> Returns the text that have been modified
"""

text = "ABCDE"
return text.strip("A") # Returns "BCDE"

text = "ABCDEAAAA"
return text.strip("A") # Returns "BCDE"

text = "ABAACAABA"
return text.strip("AB") # Returns "C"
```

### Using .replace()
```Python
"""
How to use:
<variable name>.replace(<text that you like to change>,<text that you like to change to>)
-> Returns the text that have been modified
"""

text = "Hello, my name is Kumamon"
return text.replace("Kumamon", "Rillakuma")
# Returns "Hello, my name is Rillakuma"
```

### Using .join()
```Python
"""
How to use:
<separator you want to use>.join(<array variable>)
-> Return the new text that have been joined
"""

text = ['I', 'am', 'a', 'happy', 'Kumamon']
print(" ".join(text)) # Prints out "I am a happy Kumamon"
```

---

# Introduction to Tuples
Tuples is an array, with a catch. They **cannot be replaced, removed, modify** after being created.

Syntactically, a tuple is a comma-separated list of values:
```Python
text = ('k', 'u', 'm', 'a', 'm', 'o', 'n')
```

and it basically works the same as list.
