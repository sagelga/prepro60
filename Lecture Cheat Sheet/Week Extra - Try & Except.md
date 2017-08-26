# Try and Except

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

```python
try:
    num = int(num)
```
The variable `num` will be converted if it does not returns out as error.

If you want to handle a specific error, you can use except keyword.

```python
try:
    num = int(num)
except:
    print("this thing cannot be convert to integer.")
```
