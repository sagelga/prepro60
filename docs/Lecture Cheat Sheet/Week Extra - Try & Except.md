# Try and Except

Copyright by P' Kumamon IT14. <br>
For education purpose only.

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
