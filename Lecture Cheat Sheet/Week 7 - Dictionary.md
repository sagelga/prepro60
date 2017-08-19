# Python Week 7 by P’ Kumamon (Dict)

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

# Introduction to Dictionary
Dictionary is similar to list. But they will require these two to complete:

- Key
- Value

Where key is for keeping the value (like variable, but you may use numbers and strings)
And the value will store the value of the key.

# Creating your new dictionary
```python
my_dictionary = dict()
```

or you can start defining your dictionary

```python
my_dictionary = {
"happy" : 20,
"not happy" : 30,
"sad" : False,
}
```

# Accessing the value from key
```python
my_dictionary['happy'] # Returns 20
```

or checking if this key or value exists in dictionary

```python
"happy" in my_dictionary # Return true
20 in my_dictionary # Return true
```

# Adding key and value to the dictionary
You can add it like list.
```python
alphabet = input()
my_dictionary = dict()

for i in alphabet:
    if not i in my_dictionary:
      my_dictionary[i] = 1
    else:
      my_dictionary += 1

```
