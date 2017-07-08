# Python Week 2 by P’ Kumamon (ฟังก์ชั่น)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](https://www.dropbox.com/s/x5xk4trg3u82bcn/GitHub-Profile-Mobile.PNG?raw=1)

----------

# ฟังก์ชั่นคืออะไร

ฟังก์ชั่น **เป็นกลุ่มของโค้ด** ฟังก์ชั่น โดยส่วนใหญ่แล้ว จะรับค่ามาเพื่อคำนวณ และส่งค่าที่คำนวณได้กลับไป โดยฟังก์ชั่นสามารถถูกใช้ได้หลายครั้ง ไม่จำกัดจำนวน และสามารถเรียกจากจุดไหนของโปรแกรมก็ได้

ฟังก์ชั่น **เป็นการย่อโค้ดให้สั้นลง** เนื่องจากว่ามันสามารถคำนวณได้ และสามารถถูกเรียกได้จากจุดไหนก็ได้ โดยภาษา Python ก็มีฟังก์ชั่นที่ให้มาอยู่แล้ว (Built In Function)

ฟังก์ชั่น **เป็นการช่วย Debug โปรแกรม** เนื่องจากว่า เราสามารถรู้ได้ว่า ปัญหาโค้ดนั้น อยู่ที่บรรทัดใดของโปรแกรม นั่นหมายความว่า ถ้าเรารู้ว่าปัญหาอยู่ที่ฟังก์ชั่นนี้ เราก็สามารถเข้าไปแก้เพียงฟังก์ชั่นนั้นๆ ได้ในทันที ไม่ต้องมานั่งหาทั้งโปรแกรม

Definitions by Utah University http://www.cs.utah.edu/~germain/PPS/Topics/function.html


# เรื่มต้นกับฟังก์ชั่น

### สร้างฟังก์ชั่นใหม่
```python
def kumamon():
    print("Hello. My name is Kumamon")
```
ฟังก์ชั่นนี้ชื่อ kumamon()

การประกาศฟังก์ชั่น จะใช้ def (ย่อจากคำว่า define function) และตามด้วยชื่อฟังก์ชั่น

สำหรับ () หลังชื่อ จะมีหน้าที่รับค่ามาจากฟังก์ชั่นอื่นๆ และ : เพื่อบอกว่าหลังบรรทัดนี้(มี Indent 1 ครั้งด้วยนะครับ) มีโค้ดที่เมื่อเราเรียกฟังก์ชั่นแล้ว ต้องทำตาม

### วิธีเรียกฟังก์ชั่น
```python
kumamon()
```
ง่ายๆเลย โดยการเขียนชื่อฟังก์ชั่น และตามด้วย () โดยใน () จะเป็นข้อมูลที่เราจะเอาให้กับฟังก์ชั่นอื่น

### โปรแกรมเพื่อเรียกฟังก์ชั่นและใช้งานฟังก์ชั่น
```python
def kumamon():
  print("Hello. My name is Kumamon")
kumamon()
```

### Throw in variables
```python
def kumamon(value):
  print("This costs", value, "baht")

kumamon(200)
# Returns "This costs 200 baht"
```
บรรทัดที่ 4 มีการเรียกฟังก์ชั่น kumamon โดยที่ให้ค่า integer ที่เท่ากับ 200

โดยเมื่ออ่านบรรทัดที่ 1 แล้ว จะหมายความว่า ค่า integer จะถูกเก็บไว้ในตัวแปร value และถูกใช้ในฟังก์ชั่น print()

### Throw in and out of variables
```python
def main(value, value2):
  print("The answer is", kumamon(value, value2))

def kumamon(num1, num2):
  return num1+num2-5

main(int(input()), int(input()))
```
ตอนนี้ main() ถูกเรียก และได้รับค่า input() ทั้งหมด 2 ตัว โดยจะถูกเรียกว่าตัวแปร value และ value2 ตามลำดับ โดยฟังก์ชั่น main() มีการเรียกฟังก์ชั่น kumamon() ด้วย ดังนั้น โปรแกรมจึงรันฟังก์ชั่น kumamon()

return คือการคืนค่าให้กับฟังก์ชั่นที่เรียกตัวมันเอง โดยโปรแกรมได้อ่านแล้วว่าให้คืนค่าผลลัพท์ของ num1+num2-5 กลับไปหาฟังก์ชั่นที่เรียกตัวมัน (ฟังก์ชั่น main) แล้วจึงทำการ print() บรรทัดของฟังก์ชั่น main()

# ฟังก์ชั่นบน Python แล้ว

การที่จะตั้งชื่อฟังก์ชั่นนั้นไม่ได้ตั้งชื่ออะไรก็ได้นะครับ โดยชื่อฟังก์ชั่นที่ Python จองไว้ไม่ให้ตั้งชื่อเหมือน จะมีดังนี้ครับ

และเช่นเดียวกัน เราก็สามารถใช้ฟังก์ชั่นที่ Python ทำไว้แล้วได้เช่นเดียวกัน โดยการเรียกเหมือนกับฟังก์ชั่นธรรมดาเลย

| abs()         | dict()      | help()       | min()      | setattr()      |
| ------------- | ----------- | ------------ | ---------- | -------------- |
| all()         | dir()       | hex()        | next()     | slice()        |
| any()         | divmod()    | id()         | object()   | sorted()       |
| ascii()       | enumerate() | input()      | oct()      | staticmethod() |
| bin()         | eval()      | int()        | open()     | str()          |
| bool()        | exec()      | isinstance() | ord()      | sum()          |
| bytearray()   | filter()    | issubclass() | pow()      | super()        |
| bytes()       | float()     | iter()       | print()    | tuple()        |
| callable()    | format()    | len()        | property() | type()         |
| chr()         | frozenset() | list()       | range()    | vars()         |
| classmethod() | getattr()   | locals()     | repr()     | zip()          |
| compile()     | globals()   | map()        | reversed() | __import__()   |
| complex()     | hasattr()   | max()        | round()    |                |
| delattr()     | hash()      | memoryview() | set()      |                |

Resource by Python Foundation https://docs.python.org/3/library/ฟังก์ชั่น.html
