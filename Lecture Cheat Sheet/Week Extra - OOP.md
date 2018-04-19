# Python Extra (Class)

Copyright by P' Kumamon IT14. <br>
For education purpose only.

## Introduction to Object Oriented Programming
In the word **object**, it is like a features in a single item. <br>
Like, printer for example. Printers can `scan` and `print` and `copy`. These are called objects <br>
and printers is called **class**.

Class can have many objects. Unlimted is another word.<br>
But to use a object and functions inside a object is another part.

Let's try creating a new class!

## Creating class
```python
class Kumamon: # Class needs AT LEAST 1 self (which equals to class name itself.)
    def __init__(self, name): # This function is __init__ WHICH IS REQUIRED BY CLASS. It defines all other variable na,e
        self.name = name + " desu" # Defining variable name to be equal to itself + desu
```

## Calling a class variables
```python
happy = Kumamon("Uvuvwevwevwe onyetenyevwe ugwemubwem ossas")
return happy.name # Returns "Uvuvwevwevwe onyetenyevwe ugwemubwem ossas desu"

```

## Example of function defining
```python
class mango:
    def func(self):
        a, b = 8, 9
        return a+b

    def func2(self, x,y):
        c = self.func()
        z = x + y + c
        return z

a = mango().func2(1,1)
print(a)
```
