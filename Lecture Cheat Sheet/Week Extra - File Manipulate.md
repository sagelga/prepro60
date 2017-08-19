# Python Extra (File Manipulation)

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

# Using Vanila Python

```python
file_variable = open("file_name.txt", "w")

file_variable.write("Hello World")

file_varialbe.close()
```
Program need to close the file. Because when you write something, it keeps it in buffer, not the actual file. By closing it, the Python script will save the buffer (write) to the according file

```python
file_1 = open("test.txt", "r+w")
file_2 = open("test2.txt", "r+w")

file_1.write("Hello")
file_2.write("Hello")

file_1.close()
```
The file `file_2` will not be saved. Because the file is not closed. Thus the program is not saved.

### Another way to write file
```python
with open("file_name.txt", "w") as file_variable:
    file_variale.write("Hello World")
```
By using `with` and `as` keyword, this script will automaticaly close the program
