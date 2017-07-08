# Description
<p align="center">Welcome to the e-judge ยินดีต้อนรับน้องๆเข้าสู่ e-judge นะครับ </p>

วันนี้พี่อยากให้น้องๆลองส่งไฟล์เข้าejudgeกันดู โดยก่อนอื่นเลยให้น้องๆสร้างไฟล์ python (.py) ขึ้นมาก่อน
โดยภายในไฟล์นี้พี่อยากให้น้องลองเขียนคำสั่งprintว่า Hello e-judge

```python
print("Hello e-judge")
```

หลังจากที่น้องสร้างไฟล์, เขียนโค้ดและเซฟไฟล์เป็น.pyเสร็จเรียบร้อยแล้ว พี่อยากให้น้องๆลองส่งไฟล์ที่น้องสร้างขึ้นมาเข้าระบบe-judgeนะครับ

## วิธีการส่งไฟล์เข้าระบบ

ให้น้องหา Panel ที่เขียนว่า Submit file ขึ้นมาก่อน (อาจจะอยู่ทางขวา ไม่ก็ด้านล่าง) ให้น้องกด browse... เลือกไฟล์ที่น้องต้องการ แล้วก็ submit แค่นี้ก็เรียบร้อยครับ

![Submit panel](https://www.dropbox.com/s/6k9zm3r0e45eh2l/1.jpg?raw=1)

## Video

[https://www.youtube.com/watch?v=K6Szlx9g5vs](https://www.youtube.com/watch?v=K6Szlx9g5vs)


Run .py files from cmd
- เปิดcmdขึ้นมาก่อน


- ใช้คำสั่งcd ในการเลือกที่อยู่ของไฟล์ให้ถูกต้อง (ในที่นี้ พี่เซฟไว้ในdesktop เราก็พิมพ์cd desktop)
```
C:\Users\xxxxx>cd desktop
```
- แล้วก็พิมพ์ py ชื่อไฟล์.py ลงไป (ในที่นี้ พี่ตั้งชื่อไฟล์ว่าhello)
```
C:\Users\xxxxx\Desktop>py hello.py
```
- มันก็จะรันไฟล์ของเราจนเสร็จสิ้น ลองตรวจสอบดูว่าoutputของเราถูกต้องหรือไม่

วิธีสร้างfunction (Define function)

1.ใช้คำสั่ง def แล้วตามด้วยชื่อฟังก์ชัน ซึ่งวิธีการตั้งชื่อตั้งเหมือนvariableเลย

2.เมื่อสร้างเสร็จ อย่าลืมcall functionด้วย
```python
def functionname():  <- (define function กำหนดฟังก์ชันชื่อfunctionnameขึ้นมา)
    # codeing here
functioname()        <- (call function เรียกใช้งานฟังก์ชันfunctionname)
```
* กรณีที่กำหนดตัวแปรไว้นอกfunction มันจะถือว่าเป็นglobal variable((Constant)) ซึ่งการตั้งชื่อglobal variableให้ถูกหลักpylint ต้องใช้A-Z(ตัวพิมพ์ใหญ่)และต้องมีเลข0-9 แต่ถ้าเป็นการกำหนดvariable ในfunction(Local variable) สามารถใช้ตัวพิมพ์เล็กได้

### Example
- Using local variable
```python
"""module docsstring"""
def main():
    """function docstring"""
    text = input() # This is local variable
    print(text)
main()
```
- Using global variable
```python
"""module docsstring"""
TEXT_1 = input() # This is global variable (Constant)
def main():
    """function docstring"""
    print(TEXT_1)
main()
```
Q: แล้วglobal variableกับlocal variableมันต่างกันอย่างไร

A: ทุกๆฟังก์ชันในmoduleสามารถเรียกใช้global variable(Constant)ได้ ในขณะที่local variableนั้น สามารถใช้ได้แค่ในfunctionที่ประกาศตัวแปรไว้

อย่าลืมdocstringในfunctionด้วยนะครับ เป็นการอธิบายว่าfunctionนี้ทำอะไร ยังไง

เดี๋ยวจะมีพี่ๆจะมาสอนเรื่องfunctionโดยละเอียดในอาทิตย์ถัดไปนะครับ

## Pylint
- เป็นตัวเช็คqualityของภาษาpythonให้ถูกหลักPEP8 ซึ่งในejudgeเราก็ใช้pylint อ่านเพิ่มเติมได้ที่

    - PEP8: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

    - pylint: [https://pylint.readthedocs.io](https://pylint.readthedocs.io)

- missing-final-newline   --->   ลืมเว้นบรรทัดสุดท้ายหรือเปล่า?
- missing-docstring       --->   ลืมdocstringหรือเปล่า?
- invalid-name            --->   ชื่อvariableหรือfunctionถูกหลักหรือเปล่า?
- mixed-indentation       --->   ระวังอย่าไปใช้tabในการย่อหน้านะครับ ใช้whitespace4ช่องในการย่อหน้า
- bad-whitespace          --->   เว้นวรรคให้ถูกต้อง มีwhitespaceเกินมาหรือเปล่า?
- เดี๋ยวจะมีพี่ๆจะมาอธิบายเรื่อง pylint, PEP8 โดยละเอียดในภายหลังนะครับ

ปล.น้องๆสามารถใช้online editorที่อยู่ด้านล่างได้นะครับ ลองเล่นดู สะดวกดีเหมือนกัน

ปล2.ลองรันโปรแกรมก่อนส่งด้วยนะครับ (idle สามารถกดF5รันได้เลย หรือจะรันผ่านcmdก็ได้)**

ปล3.อย่าลืมdocstring และfinal new-line ด้วยนะครับ**

# Specification
| Input Specification | Output Specification |
| - | - |
|| 1บรรทัด เป็น string ที่มีข้อความตามที่กำหนด |

# Sample Case
| Sample Input | Sample Output |
| - | - |
|| Hello e-judge |