# Dealing with Pylint + PEP8
PEP8 คือ standard ของการเขียนโปรแกรม เพื่อให้คนอื่นๆ อ่านออกนะครับ ดังนั้นมันจึงเป็นเรื่องสำคัญที่จะต้องเขียนให้ผู้เขียนและผู้อ่าน เข้าใจว่าโปรแกรมนี้ทำงานอย่างไร<br>
โดย PEP8 นั้นถูกเขียนไว้ที่ Python Foundation : [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

``` note
พี่มงเจอแค่ปัญหาพวกนี้นะครับ ถ้าอันไหนพี่ยังไม่ได้อธิบาย ฝากเขียนไว้ใน Issues ให้พี่ด้วยจ้า [https://github.com/sagelga/PreProgramming-60/issues](https://github.com/sagelga/PreProgramming-60/issues)
```

---

## 1. Missing DocString
Docstring คือ comment เพื่อบอกว่าฟังชั่น หรือ โปรแกรมนั้นๆ ทำงานเพื่ออะไร โดยทุก function ละหัวไฟล์ (บรรทัดที่ 1) จะต้องมี docstring กำกับ

เช่น

```python
"""
This program will print out the "Happy Kumamon" to the world
"""

def happyKumamon():
  """This function will print out the text"""
  print("Hello Kumamon")
happyKumamon()
```

โดย DocString ที่ดีนั้น ใน Docstring ต้องอธิบายโปรแกรม จะต้องอธิบายว่าทั้งโปรแกรมนั้นมีหน้าที่อะไร อย่างไรแบบคร่าวๆ<br>
สำหรับ DocString ที่อธิบายฟังก์ชั่นนั้น ก็ต้องอธืบายว่าฟังก์ชั้นนั้นทำงานเพื่ออะไร หรือว่ากำลังจะทำอะไรอยู่

---

## 2. Missing new line
เป็นเรื่องของการลืมสร้างบรรทัดใหม่
น้องๆอาจจะไม่เข้าใจ ว่าทำไปทำไม เพื่ออะไร แต่มันเป็นการบอกโปรแกรมว่าบรรทัดสุดท้ายได้หมดแล้ว

StackOverflow Reference :  [https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline](https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline)

โดยที่พวก Text Editor ส่วนใหญ่ จะมีการทำให้อยู่แล้ว

```python
"""This program will print out the "Happy Kumamon" to the world"""
def happy():
  """This function will print out the text"""
  print("Hello Kumamon")
happy()
# and leave this line blank
```

---

## 3. Invalid Data Type
เป็นการบอกว่าไม่สามารถทำการแปลงประเภทตัวแปร (Data Type Casting) ได้

เช่น
```python
int(input())
```
ถ้าหากรับค่า int มันจะแปลงจาก string เป็น int ปกติ
ถ้าหากรับค่า string มันจะแปลงไม่ได้ เพราะ string เป็นตัวอักษร เปลี่ยนค่าเป็นตัวเลขไม่ได้นะจ๊ะ

---

## 4. Invalid Syntax
การใช้ฟังชั่นที่ใช้ชื่อผิด ใช้ผิดวิธี โมดูลขาด argument หรือ ไม่ได้เรียกโมดูลที่ต้องการใช้มาก่อน

เช่น
```python
import math
var_x = pi()
```
ซื้ง pi() ไม่ใช่ฟังชั่นใน python หลัก แต่เป็นส่วนหนึ่งของ library ชื่อ math

ดังนั้นจึงต้องใช้
```python
import math
var_x = math.pi()
```

---

## 5. Unused Variables
เป็นการประกาศตัวแปร แล้วน้องไม่เคยใช้มันเลย มันอาจจะไม้เป็นไรสำหรับการรัน เพราะก็สามารถรันได้อย่างปกติ
แต่มันเปลืองพื้นที่ RAM (เพื่อจองพื้นที่สำหรับ variable นี้) ทำให้ Pylint ด่า

ซึ่ง การประกาศแล้วไม่ได้ใช้ วิธีแก้ก็คือ ไม่ต้องไปประกาศครับ ง่ายเนอะ

เช่น
```python
kumamon = "Happy"
var_x = 12
var_y = 21
print(var_x + var_y)
```
ซึ่งตัวแปร kumamon ไม่ได้ถูกใช้ในบรรทัดอื่น (นอกจากการประกาศค่า) เป็นการสี้นเปลืองทรัพยากร

---

## 6. Variable Error & Variable Name
การตั้งชื่อ Variable ก็เป็นสี่งจำเป็นในการทำ python เนอะ เพราะก็เอาไว้เก็บค่าตัวแปร

แต่การตั้งชื่อตัวแปรที่ง่ายๆ มันมักจะทำให้จุดอื่นๆพังไปด้วย

เช่น

```python
import math
math = "Kumamon" # ตั้งชื่อตัวแปรเหมือนชื่อ library
print(math.fabs(20-99))
```
ก็จะทำให้มันงง ว่าจะให้โหลด library หรือเรียกตัวแปรที่ชื่อว่า math

หรือ
```python
aaa = 12
bbb = 55

print(aaa + bbb)
```
ซื่งตัวแปร `aaa` นั้นก็ปกติอยู่หรอก แต่จะให้คนอื่นเค้ามาอ่านด้วยนั้น เป็นเรื่องที่ยากเหลือเกิน ว่าต้วแปรนี้เอาไว้ทำอะไร

ดังนั้นพี่มงเลยมี Checklist ที่มันน่าจะด่านะครับ :)

Number|Type|Meaning|Example
-|-|-|-
1|Short Variable|ชื่อตัวแปรสั้นเกินไป|เช่น a
2|Long Variable|ชื่อตัวแปรยากเกินเหตุ|เช่น Uvuvwevwevwe_Onyetenyevwe_Ugwemubwen_Ossas
3|Variable Name is the same as function|ชื่อตัวแปรเหมือนชื่อฟังชั่น|เช่น if
4|Easy variable name|ตั้งชื่อตัวแปรอย่างง่ายๆ|เช่น aaa
5|Capitalized Variable|ตัวแปรที่มีการตั้งเป็นตัวใหญ่ด้านหน้า (เนื่องจากจะซ้ำกับวิธีประกาศ class)|เช่น Num_1
6|Camel Cased Variable|ตัวแปรที่ใช้การตั้งค่าเป็นตัวใหญ่แบ่งคำ (เนื่องจากจะซ้ำกับวิธีประกาศชื่อ function)|เช่น distanceOverTime
7|All Capitalized Variable (inside function)|ตัวแปรที่เป็นตัวใหญ่หมดเมื่อประกาศใน Local Variable|เช่น DISTANCE
8|Weird Variable Name|ตัวแปรไม่บ่งบอกถึงการใช้งาน|เช่น num_1 สำหรับการเก็บค่า distance

ดังนั้น น้องๆจะต้องระวังในการตั้งชื่อนะครับ

---

## 7. Bad White Space
การที่มี white space ในจุดที่มันไม่จำเป็น เป็นการเสียทรัพยากรในการให้ Python ทำงานนะครับ และ ทำให้เพื่อนๆของน้อง อ่านโค้ดของน้องได้ยากขื้น

เช่น
(พี่จะแทน space ด้วย * นะครับ จะได้เห็นกันง่ายๆ)

```python
print("Hello World")*
var_x,var_y = 12,21
print(var_x,var_y)
```

ในนี้ Pylint จะด่า
```python
print("Hello World")*
```
เนื่องจาก มี white space หลังบรรทัดนะครับ มันไม่จำเป็นต้องมีเลย

```python
var_x,var_y = 12,21
print(var_x,var_y)
```
จะด่า เพราะ การใช้ , ควรจะเหมือนเขียนภาษาอังกฤษนะครับ ต้องมี space หลัง , นะจ๊ะ ดังนั้นมันควรเป็นแบบนี้
```python
var_x, var_y = 12, 21
print(var_x, var_y)
```

---

## 8. Too much Local Variable
เป็นก่ารประกาศค่าตัวแปรมากเกินไป เปลืองทั้งทรัพยากร แล้วน้องๆก็ไม่จำเป็นต้องมีมากขนาดนั้นด้วย

เช่น
```python
def kumamon():
  var_a = 12
  var_b = 13
  var_c = 14
  var_d = 15
  var_e = 15
  var_f = 16
  var_g = 17
  var_h = 18
  var_i = 19
  var_j = 20
  var_k = 21
  var_l = 22
  var_m = 23
kumamon()
```
หากเก็บแบบนี้ ไฟล์จะใหญ่ และทำงานได้ช้ามาก ดังนั้น ควรมาใช้ Array หรือ Dict แทนนะครับ

---

## 9. Too much Global Variable
เหมือนกับข้อที่แล้วเลยจ้า มันเปลืองพื้นที่ (เปลืองมากกว่า local อีกนะครับ จะบอกให้)

เช่น
```python
  VAR_A = 12
  VAR_B = 13
  VAR_C = 14
  VAR_D = 15
  VAR_E = 15
```

---

## 10. Line is too long
เป็นการบอกว่าโปรแกรมในแถวใดแถวหนึ่งยาวมาก <br>
โดยปกติแล้ว โปรแกรมก็ไม่ควรที่จะยาวเกิน **100 ตัวอักษร** อยู่แล้ว เพราะเดี๋ยวจะอ่านไม่ออกและดูน่ารำคาญ

เช่น
```python
  print("This is a very long string, and they are more than 100 character long. They just keep going and going and going and going and going and going and going and going and going and going")
```

---

## 11. Too many branch
เมื่อน้องต้องการทำ If statement แล้วใช้มากเกินเหตุ หรือ ซ้อนกันมาก (Chained)

เช่น
```python
    var_x = int(input())
    if var_x == 1:
        print("Var_x is equal to", var_x)
    else:
        if var_x == 2:
            print("Var_x is equal to", var_x)
        else:
            if var_x == 3:
                print("Var_x is equal to", var_x)
            else:
                if var_x == 4:
                    print("Var_x is equal to", var_x)
                else:
                    if var_x == 5:
                        print("Var_x is equal to", var_x)
                    else:
                        if var_x == 6:
                            print("Var_x is equal to", var_x)
                        else:
                            if var_x == 7:
                                print("Var_x is equal to", var_x)
                            else:
                                if var_x == 8:
                                    print("Var_x is equal to", var_x)
                                else:
                                    if var_x == 9:
                                        print("Var_x is equal to", var_x)
                                    else:
                                        if var_x == 10:
                                            print("Var_x is equal to", var_x)
                                        else:
                                            if var_x == 11:
                                                print("Var_x is equal to", var_x)
                                            else:
                                                if var_x == 12:
                                                    print("Var_x is equal to", var_x)
                                                else:
                                                    if var_x == 13:
                                                        print("Var_x is equal to", var_x)
                                                    else:
                                                        if var_x == 14:
                                                            print("Var_x is equal to", var_x)
                                                        else:
                                                            if var_x == 15:
                                                                print("Var_x is equal to", var_x)

```
หากว่าน้องอยากจะใช้เยอะจริงๆ การใช้งานหลายฟังชั่น ก็เป็นวิธีหนึ่งในการช่วยให้น้องเขียนโค้ดน้อยลงเนอะ

---

## 12. Mixing Tabs and Space
การใช้ Python น้องๆก็รู้ๆอยู่นะครับ ว่าจะไม่มีการใช้ {} ในการให้โปรแกรมรู้ว่าอยู่ในระดับขั้นตอนไหน<br>
ซึ่งการ indent ที่ดี ก็เป็นสี่งจำเป็น เพื่อให้ Python เข้าใจน้องๆนะครับ<br>
การ Indent จะใช้เท่ากับการกด space 4 ครั้งครับ ไม่ใช่ Tab<br>
เช่น (พี่จะแทนที่ space ด้วย * และ tab ด้วย ____ นะครับ

อันนี้เป็นตัวอย่างที่ถูกต้องนะครับ
```python
def kumamon():
****print("Hello world")
kumamon()
```

อันนี้ผิด
```python
def kumamon():
____print("This is a very long string, and they are more than 100 character long. They just keep going and going and going and going and going and going and going and going and going and going")
kumamon()
```
ซึ่งเวลาน้องเห็นบน Text Editor มันจะเหมือนกันมากๆเลย แทบจะดูไม่ออก ดังนั้น น้องต้องระวังนะครับ

---

## 13. Too many arguments in function
การส่งค่าให้กับฟังชั่นอื่นๆ มากเกินไป

เช่น
```python
def kumamon():
  var_a = int(input())
  var_b = int(input())
  var_c = int(input())
  var_d = int(input())
  var_e = int(input())
  var_f = int(input())
  var_g = int(input())
  var_h = int(input())
  calculate(var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h)

def calculate(var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h):
  print("The answer is", var_a + var_b + var_c + var_d + var_e + var_f + var_g + var_h)

kumamon()
```

---

## 14. Conflicted Variable Name
โดยจะเกิดขื้นเมื่อต้องการให้ตัวแปรนึงไปเป็นตัวนับ (ซึ่งตัวนับจะถูกลบล้างไป หากมีการใช้งาน) ดังนั้น ตัว PyLint จึงด่าครับ
```python
x = 12
for x in range(1, 10):
    print(x)
```

หากต้องการแก้ไข ให้เปลี่ยนชื่อตัวแปรไม่ให้ซ้อนทับกันครับ
```python
x = 12
for i in range(1, 10):
    print(i)

```

---

15. Incorrect line indentation
โดยอันนี้จะเกิดขื้นเมื่อน้องอยากให้ตัวโปรแกรมเหลือบรรทัดน้อยๆ หรือเกิดจากน้องลืมกด ENTER เพื่อเปลี่ยนบรรทัด เช่น<br>
แต่โดยปกติแล้ว โปรแกรมจะไม่รันเลย เนื่องจากว่าไม่เข้าใจว่าต้องการทำอะไร<br>
แต่สำหรับบางเหตุการนั้น ได้เฉยเลย พี่เลยเขียนไว้ก่อนนะครับ ว่าให้ศึกษาก่อนที่จะ shorthand coding นะจ๊ะ
```python
# Normally what it should be
if (x > 12):
    print(x)

# This is incorrect way to shorthand if functions
if (x > 12): print(x)

# This is correct way to shorthand if function
print(x) if (x > 12)
```

Pylint จะด่า เพราะน้องส่งตัวแปรให้กับฟังชั่น calculate มากเกินไป :(

---

# How Ejudge sees your code
เวลาที่น้องๆเขียนแบบนี้
```python
  var_x = str(input())
```
การที่ input() ธรรมดา เวลารับ มันเป็น string อยู่แล้วนะครับ ไม่ต้องไปครอบมันนะ


```python
  var_x = input("This will go as var_x")
```
น้องอาจจะให้การทำให้ input โชว์ว่า กำลัง input อะไรอยู่ Ejudge จะเห็นแบบนี้ครับ
```
  This will go as var_x
```

ซึ่งเป็น string ทำให้เวลาน้องทำอะไร มันก็จะบอกว่าผิดนะครับ ดังนั้น น้องควรทำแบบนี้

```python
  var_x = input()
```

# Switching from other coding language
หากน้องเคยเรียนภาษาคอมพิวเตอร์อื่นๆมาก่อนแล้ว การที่น้องมาเรียนอีกภาษานึง อาจเป็นเรื่องยากสำหรับน้องเอง
ซี่งเป็นพี่ พี่ก็เป็นครับ อะไรก็ไม่รู้เหมือนกัน ทำไมอันนี้มี อันนี้ไม่มี วันนี้พี่มงจะมาเปรียบเทียบให้น้องดูกันครับ

### Code Blocks and Indentations
Code Block คือเป็นการบอกตัว compiler ว่าโค้ดส่วนนี้ จัดว่าไปอยู่กับจุดไหนของโปรแกรม

หากเป็น C หรือ Java หรือ อะไรอื่น จะอ่านแบบนี้
```c
int kumamon = 12;
if (kumamon > 12){
    printf("Happy!!\n");
}
else{
    printf("Not very happy!!\n");
}
```

โดยที่โปรแกรมจะเข้าใจบรรทัด
```c
printf("Happy!!\n");
```
และ
```c
printf("Not very happy!!\n");
```
ว่าถ้า If statement ทำงาน จะเกิดพวกนี้ขื้น

แต่สำหรับ Python แล้ว
```python
kumamon = 12;
if kumamon > 12:
    print("Happy!!");
else:
    print("Not very happy!!");
```
การ Indent ข้างหน้าบรรทัด เป็นการบอกเหมือนกับการใช้งาน {} เลย

### End of the line
บางภาษาโปรแกรมมี่ง ต้องใช้งาน ; เพื่อจะบอกว่าบรรทัดนี้ ได้หมดลงแล้ว แต่ถ้าหากยังไม่มี ก็จะอ่านต่อไป จนกว่าจะเจอ

พี่มงจะเปรียบเทียบกับภาษา C ให้ดูนะครับ
```C
int kumamon = 12;
if (kumamon > 12){
    printf("Happy!!
    \n");
}
else{
    printf("Not very
    happy!!\n");
}
```
มันคงยังมีความหมายเหมือนเดิม เพราะว่าตัว Compiler จะเข้าใจว่า การที่มี ; ปิด คือหมดบรรทัดนั้นแล้ว

แต่ถ้าเป็น Python
```python
if kumamon > 12:
    print("Happy!!");
else:
    print("Not very \
    happy!!");
```
