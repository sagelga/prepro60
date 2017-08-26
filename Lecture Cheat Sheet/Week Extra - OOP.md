# Python Extra (Class)

## Lecture List

|Week 1|Week 2|Week 3|Week 4|Week 5|Week 6|Week 7|Week 8|Week 9|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|[Click](/Lecture%20Cheat%20Sheet/Week1%20-%20IO.md)|[Click](/Lecture%20Cheat%20Sheet/Week%202%20-%20Functions.md)|[Click](/Lecture%20Cheat%20Sheet/Week%203%20-%20Math%20Library.md%20)|[Click](/Lecture%20Cheat%20Sheet/Week%204%20-%20Strings.md)|[Click](/Lecture%20Cheat%20Sheet/Week%205%20-%20Condition.md%20)|[Click](/Lecture%20Cheat%20Sheet/Week%206%20-%20Loops.md)|[Click](/Lecture%20Cheat%20Sheet/Week%207%20-%20Lists%20+%20Tuples.md)|[Click](/Lecture%20Cheat%20Sheet/Week%208%20-%20Dictionary.md)|[Click](/Lecture%20Cheat%20Sheet/Week%209%20-%20Recursion.md)|

## Follow me on GitHub
|<a href="https://github.com/sagelga"><img src="https://avatars0.githubusercontent.com/u/13056824" width="100px"></a>  |
|:-:|  
|@sagelga|

Copyright by P' Kumamon IT14. <br>
For education purpose only.

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)

----------
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
