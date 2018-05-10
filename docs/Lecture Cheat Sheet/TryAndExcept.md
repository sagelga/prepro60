# Try and Except
คำว่า Try คือการลองโค้ดบรรทัดนัั้น เพื่อหากว่าการลองนั้นไม่ผ่าน (เกิด Exception) ก็จะไม่ทำโปรแกรมเราพัง

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
