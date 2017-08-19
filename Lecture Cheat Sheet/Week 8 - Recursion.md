# Python Week 8 by P’ Kumamon (Recursion)

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

# Introduction to Recursion

Q : What is recursion? <br>
A: Q : What is recursion? <br>
A: A: Q : What is recursion? <br>
A: A: A: Q : What is recursion? <br>
A: A: A: A: Q : What is recursion? <br>
A: A: A: A: A: Q : What is recursion? <br>
A: A: A: A: A: A: Q : What is recursion? <br>
A: A: A: A: A: A: A: Q : What is recursion?

> Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of this function call. If a function definition fulfils the condition of recursion, we call this function a recursive function. - python-course.eu

# Example of use in recursion
Calculating 4 x 3 x 2 x 1 without using built-in function or loops
```python
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
factorial(4)
```

# The Pitfalls of Recursion

This subchapter of our tutorial on recursion deals with the Fibonacci numbers. What do have sunflowers, the Golden ratio, fur tree cones, The Da Vinci Code and the song "Lateralus" by Tool in common. Right, the Fibonacci numbers.

The Fibonacci numbers are the numbers of the following sequence of integer values:

```
0,1,1,2,3,5,8,13,21,34,55,89, ...
```

The Fibonacci numbers are defined by:
```
Fn = Fn-1 + Fn-2
with F0 = 0 and F1 = 1
```

The Fibonacci sequence is named after the mathematician Leonardo of Pisa, who is better known as Fibonacci.

The Fibonacci numbers are easy to write as a Python function. It's more or less a one to one mapping from the mathematical definition:

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

An iterative solution for the problem is also easy to write, though the recursive solution looks more like the mathematical definition:

```python
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
```    

If you check the functions fib() and fibi(), you will find out that the iterative version fibi() is a lot faster than the recursive version fib().
