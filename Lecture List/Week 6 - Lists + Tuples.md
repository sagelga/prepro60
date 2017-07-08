# Python Week 6 by P’ Kumamon (Lists + Tuples)

Copyright by P' Kumamon IT14 & Wiput IT15.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

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

# kumamon now equals to
[1, 2, 3, 4, 5]
```

### Using reversed sort
```Python
kumamon = [1, 3, 4, 2, 5]
kumamon.sort(reverse = True)

# kumamon now equals to
[5, 4, 3, 2, 1]
```

### Sort is from ASCII
```Python
kumamon = ['9', '1', 'a', 'A']
kumamon = kumamon.sort()

# kumamon now equals to
['1', '9', 'A', 'a']
```

# Using Elements in Array
### Using .pop()
.pop() will print then remove that item

### Using array call
```Python
kumamon = ["Happy", "Funny", "Fat"]
print(kumamon[1])

# Returns "Funny"
```

# Remove Elements in Array
### Using .remove()
.remove() will remove that element from the array

## Using .strip()
```Python
How to use:
<variable name>.strip("<character/text you want to remove>")
-> Returns the text that have been modified


text = "ABCDE"
return text.strip("A") # Returns "BCDE"

text = "ABCDEAAAA"
return text.strip("A") # Returns "BCDE"

text = "ABAACAABA"
return text.strip("AB") # Returns "C"
```

### Using .replace()
```Python
How to use:
<variable name>.replace(<text that you like to change>,<change into>)
-> Returns the text that have been modified


text = "Hello, my name is Kumamon"
return text.replace("Kumamon", "Rillakuma")
# Returns "Hello, my name is Rillakuma"
```

### Using .join()
```Python
How to use:
<separator you want to use>.join(<array variable>)
-> Return the new text that have been joined


text = ['I', 'am', 'a', 'happy', 'Kumamon']
print(" ".join(text)) # Prints out "I am a happy Kumamon"
```

---

# Introduction to Tuples
Tuples is an array, with a catch. They **cannot be replaced, removed, modify** after being created.

Syntactically, a tuple is a comma-separated list of values:
```Python
text = 'k', 'u', 'm', 'a', 'm', 'o', 'n'
```
Although it is not necessary, it is common to enclose tuples in parentheses:
```Python
text = ('k', 'u', 'm', 'a', 'm', 'o', 'n')
```
To create a tuple with a single element, you have to include a final comma:
```Python
t1 = 'a',
type(t1)
# Return
<class 'tuple'>
```
A value in parentheses is not a tuple:
```Python
t2 = ('a')
type(t2)
# Return
<class 'string'>
```
Another way to create a tuple is the build-in function tuple. With no argument, it creates an empty tuple:
```Python
t = tuple()
t
# Return
()
```

# Tuple assignment
It is often useful to swap the values of two variables. With conventional assignments, you have to use a temporary variable. For example, to swap a and b:
```Python
temp = a
a = b
b = temp
```
This solution is cumbersome; tuple assignment is more elegant:
```Python
a, b = b, a
```
The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.

The number of variables on the left and the number of values on the right have to be the same:
```Python
a, b = 1, 2, 3
# Return
ValueError: too many values to unpack
```
More generally, the right side can be any kind of sequence (string, list or tuple). For example, to split an email address into a user name and a domain, you could write:
```Python
address = 'kumamon@kumamoto.me'
username, domain = address.split('@')
```
When you print out username and domain you will get:
```Python
print("Username :", username)
print("Domain :", domain)
# Returns
Username : kumamon
Domain : kumamoto.me
```
# Tuples as return values
Strictly speaking, a function can only return one value, but if the value is a tuple, the effect is the same as returning multiple values. For example, if you want to divide two integers and compute the quotient and remainder, it is inefficient to compute x/y and then x%y. It is better to compute them both at the same time.

The built-in function divmod takes two arguments and returns a tuple of two values, the quotient and remainder. You can store the result as a tuple:
```Python
result = divmod(7, 3)
print(result)
# Return (2, 1)
```
Or use tuple assignment to store the elements separately:
```Python
quotient, remainder = divmod(7, 3)
print("Quotient :", quotient)
print("Remainder :", remainder)
# Returns
Quotient : 2
Remainder : 1
```
# Variable-length argument tuples
Functions can take a variable number of arguments. A parameter name that begins with * gathers arguments into a tuple. For example, printall takes any number of arguments and prints them:
```Python
def printall(*args):
    print(args)
```
The gather parameter can have name you like, but args us conventional. Here's how the function works:
```Python
printall(1, 2.0, '3')
# Return
(1, 2.0, '3')
```
The complement of gather is scatter. If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator. For example, divmod takes exactly two arguments; it doesn’t work with a tuple:
```Python
data = (7, 3)
print(divmod(data))
# Return
TypeError: divmod expected 2 arguments, got 1
```
But if you scatter the tuple, it works:
```Python
data = (7, 3)
print(divmod(*data))
# Return
(2, 1)
```
Many of the built-in functions use variable-length argument tuples. For example, max and min can take any number of arguments:
```Python
max(1, 2, 3)
# Return 3
```
But sum does not.
```Python
sum(1, 2, 3)
# Return
TypeError: sum expected at most 2 arguments, got 3
```
# Lists and tuples
zip is a built-in function that takes two or more sequences and returns a list of tuples where each tuple contains one element from each sequence. The name of the function refers to a zipper, which joins and interleaves two rows of teeth.

This example zips a string and a list:
```Python
s = 'abc'
t = [0, 1, 2]
zip(s, t)
# Return
<zip object at 0x7f7d0a9e7c48>
```
The result is a zip object that knows how to iterate through the pairs. The most common use of zip is in a for loop:
```Python
for pair in zip(s, t):
    print(pair)
# Return
('a', 0)
('b', 1)
('c', 2)
```
A zip object is a kind of iterator, which is any object that iterates through a sequence. Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select an element from an iterator.

If you want to use list operators and methods, you can use a zip object to make a list:
```Python
list(zip(s, t))
# Return
[('a', 0), ('b', 1), ('c', 2)]
```
The result is a list of tuples; in this example, each tuple contains a character from the string and the corresponding element from the list.
If the sequences are not the same length, the result has the length of the shorter one.
```Python
list(zip('SonKung', 'ObaKung'))
# Return
[('S', 'O'), ('o', 'b'), ('n', 'a'), ('K', 'K'), ('u', 'u'), ('n', 'n'), ('g', 'g')]
```
You can use tuple assignment in a for loop to traverse a list of tuples:
```Python
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)
```
Each time through the loop, Python selects the next tuple in the list and assigns the ele- ments to letter and number. The output of this loop is:
```Python
0 a
1 b
2 c
```
If you combine zip, for and tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time. For example, has_match takes two sequences, t1 and t2, and returns True if there is an index i such that t1[i] == t2[i]:
```Python
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
return False
```
If you need to traverse the elements of a sequence and their indices, you can use the built-in function enumerate:
```Python
for index, element in enumerate('abc'):
    print(index, element)
```
The result from enumerate is an enumerate object, which iterates a sequence of pairs; each pair contains an index (starting from 0) and an element from the given sequence. In this example, the output is
```Python
0 a
1 b
2 c
```
Again.
# Dictionaries and tuples
Dictionaries have a method called items that returns a sequence of tuples, where each tuple is a key-value pair.
```Python
d = {'a':0, 'b':1, 'c':2}
t = d.items()
t
# Return
dict_items([('c', 2), ('a', 0), ('b', 1)])
```
The result is a dict_items object, which is an iterator that iterates the key-value pairs. You can use it in a for loop like this:
```Python
for key, value in d.items():
    print(key, value)
# Return
c 2
a 0
b 1
```
As you should expect from a dictionary, the items are in no particular order.

Going in the other direction, you can use a list of tuples to initialize a new dictionary:
```Python
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
d
# Return
{'a': 0, 'c': 2, 'b': 1}
```
Combining dict with zip yields a concise way to create a dictionary:
```Python
d = dict(zip('abc', range(3)))
d
# Return
{'a': 0, 'c': 2, 'b': 1}
```
The dictionary method update also takes a list of tuples and adds them, as key-value pairs, to an existing dictionary.

# String to character stripping
```plain
Converge text (merge) -> .join()
Diverge text (separate) -> .split()

Replacing text (replace) -> .replace()
Stripping text (strip) -> .strip()
```
