# File Manipulation
## Using Vanilla Python

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
