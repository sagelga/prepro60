# Conditions
ใน Lecture นี้ พี่มงจะขออธิบายเกี่ยวกับหลักการตัดสินใจของโปรแกรมกันนะครับ<br>
โดยปกติแล้ว คอมพิวเตอร์ไม่รู้หรอกว่า หากน้องมี input เข้ามา และน้องต้องการให้มันทำงานต่างกันตามประเภทหรือข้อมูลที่เข้ามา<br>

ตัวอย่างของการตัดสินใจ เช่น

น้องต้องการว่า ถ้าตัวแปร `kumamon` นั้นเท่ากับ 1112 ก็ให้ปรี้นท์ "Hello World" ออกทางหน้าจอ<br>
แต่หากว่าไม่เท่ากับ 1112 ก็ให้ปรี้นท์ "Go straight to jail" ออกทางหน้าจอ

จากความหมายด้านบน พี่มงก็จะเขียน "โปรแกรม" ได้ดังนี้
```
ถ้า (ตัวแปร kumamon เท่ากับ 1112):
  ให้ปรี้นท์ผลลัพท์ "Hello World" ออกทางหน้าจอ

แต่หากว่าไม่เท่ากับ 1112:
  ให้ปรี้นท์ผลลัพท์ "Go straight to jail"
```

และถ้าน้องจะเขียนโปรแกรม Python ก็จะได้แบบนี้
```python
if (kumamon = 1112):
    print("Hello World")
else:
    print("Go straight to jail")
```
อ่านโค้ดออกมั้ยเอ่ย ถ้ายัง พี่มงก็จะสอนครับ

## Introduction to `IF` statement
`IF` ในภาษาไทย หมายถึง "หาก" "เมื่อ" "ถ้า"<br>
ในภาษาโปรแกรมแล้ว หากมีอะไรเป็นจริง ก็จะทำงานบรรทัดต่อไป ตัวอย่างเช่น

```python
if (kumamon = "cute"):
    print("yessssssssssssss")
```

ในโปรแกรมด้านบน ก็จะอ่านเป็นภาษาไทยว่า ถ้าตัวแปรคุมะมง มีค่าเท่ากับ "cute" ก็ให้ทำการปรี้นท์คำว่า "yessssssssssssss" ออกบนหน้าจอ

เราจะมาลองทดสอบกับ input ที่แตกต่างกัน โดยใช้โปรแกรมด้านบนกันครับ

ในตัวอย่างด้านล่างนี้ พี่มงขอกำหนดค่า kumamon เป็น "Happy Kumamon" ก่อนนะครับ
```python
kumamon = "Happy Kumamon"

# และพี่มงก็จะทำการก้อปโปรแกรมด้านบนมาทำงาน
if (kumamon == "cute"):
    print("yessssssssssssss")
```

น้องก็จะสังเกตุได้ว่า โปรแกรมมันไม่ปรี้นท์อะไรออกมาเลย<br>
แล้วน้องก็ได้เหลือบไปดูข้างบนที่พี่มงได้เขียนไว้ว่า "หากมีอะไรเป็นจริง ก็จะทำงานบรรทัดต่อไป" และน้องก็ได้เข้าใจว่า ค่าที่อยู่ในตัวแปร kumamon ("Happy Kumamon") มันไม่ได้เท่ากับค่าที่เปรียบเทียบหนิ เลยทำให้บรรทัดปรี้นท์ไม่ได้ทำงานเนื่องจาก สมการเป็นเท็จ

ในตัวอย่างต่อไป พี่มงขอกำหนดค่า kumamon เป็น "cute" ก่อนนะครับ
```python
kumamon = "cute"

# และพี่มงก็จะทำการก้อปโปรแกรมด้านบนมาทำงาน
if (kumamon == "cute"):
    print("yessssssssssssss")
```
น้องก็จะสังเกตุได้ว่า โปรแกรมได้ปรี้นท์คำว่า "yessssssssssssss" ออกทางหน้าจอแล้ว<br>
ก็เพราะสมการนั้นเป็นจริงนั่นเอง บรรทัดด้านล่างจึงทำงาน

แต่น้องๆก็จะถามพี่มงว่า แล้วใช้ if หลายบรรทัดได้หรือเปล่า ก็มาลองกันครับ
```python
if (kumamon == "cute"):
    kumamon = 1112
    print(kumamon)
```
น้องลองคิดตามดูครับ ว่าผลลัพท์จะออกมาเป็นอะไร ลองคิดก่อนอ่านบรรทัดต่อไปนะครับ <br>ถ้าน้องตอบว่า 1112  ก็ถือว่าน้องเข้าใจแล้ว อิอิ


### สี่งที่ทำให้ if statement ทำงาน (ค่าเป็น true)
|1|2|3|4|5|
|:-:|:-:|:-:|:-:|:-:|
|สมการเป็นจริง|ตัวแปรกับค่าที่เปรียบเทียบมีค่าเท่ากัน|ค่าตัวแปรที่เป็นตัวเลขเป็นจำนวนไม่ใช่ 0|ค่า Boolean ในตัวแปรเป็นจริง|ค่า logic เป็นจริง|
|**ตัวอย่างเช่น**<br>`if(2 + 2 = 4)`|**ตัวอย่างเช่น**<br>`kumamon = "cute"`<br>`if(kumamon == "cute")`|**ตัวอย่างเช่น**<br>`kumamon = 1112`<br>`if(kumamon)`|**ตัวอย่างเช่น**<br>`kumamon = true`<br>`if(kumamon)`|**ตัวอย่างเช่น**<br>`if(true or false)`|

เนืื่องจากพี่ใช้หลักการ logic ด้วย พี่มงก็ต้องขออธิบาย logic ซะก่อนนะครับ

## Logic Operator
Logic Operator เป็นการจัดการตัวแปรประเภท boolean เพื่อการจัดการ logic นั่นเอง<br>
โดยน้องๆจะได้ใช้งานอย่างเต็มที่ เมื่อได้เรียน Conditions ครับ

ตัวอย่าง Logic Operator

| Data Type 	| วิธีการเขียนแบบทั่วไป 	| หรือจะเขียนแบบนี้ก็ได้ 	|
|-----------	|------------------	|------------------	|
| AND       	| and              	| `&`                	|
| OR        	| or               	| `|`                
| NOT       	| not              	| !                	|
| XOR       	| xor              	| ^                	|

### ตารางแสดงผลลัพท์ เมื่อทำการ AND
|       	|      	|  	|
|-------	|----------	|-------	|
|       	| TRUE     	| FALSE 	|
| TRUE  	| **TRUE** 	| FALSE 	|
| FALSE 	| FALSE    	| FALSE 	|

ก็จะเห็นได่ว่า ตัวแปรทั้งสองต้องเป็น TRUE เพื่อทำให้สมการ AND เป็น TRUE

### ตารางแสดงผลลัพท์ เมื่อทำการ OR
|       	|      	|  	|
|-------	|----------	|-------	|
|       	| TRUE 	| FALSE     	|
| TRUE  	| TRUE 	| TRUE      	|
| FALSE 	| TRUE 	| **FALSE** 	|

ก็จะเห็นได่ว่า ตัวแปรทั้งสองต้องเป็น FALSE เพื่อทำให้สมการ OR เป็น FALSE

ตัวอย่างการทดสอบ Logical Operator
```python
print(False and False)  # แลดงผลลัพท์เป็น False
print(False and True)   # แลดงผลลัพท์เป็น False
print(True and False)   # แลดงผลลัพท์เป็น False
print(True and True)    # แลดงผลลัพท์เป็น True

print(False or False)   # แลดงผลลัพท์เป็น False
print(False or True)    # แลดงผลลัพท์เป็น True
print(True or False)    # แลดงผลลัพท์เป็น True
print(True or True)     # แลดงผลลัพท์เป็น True
```

### ตารางแสดงผลลัพท์ เมื่อทำการ NOT
| **Input** | **Output หลังจากการใช้ NOT** |
| -------- | ----------- |
| False    | True        |
| True     | False       |

```python
print(not False) # Return True
print(not True)  # Return False
```

จะเห็นได้ว่า การทำ NOT นั้นจะสลับ logic (เช่น จริงไปเป็นเท็จ และ เท็จไปเป็นจริง)

## Comparison Operator
| **==**    | **!=**       | **<**     | **<=**                | **>**     | **>=**                |
| --------- | ------------ | --------- | --------------------- | --------- | --------------------- |
| Equals to | Not equal to | Less than | Less than or equal to | More than | More than or equal to |

## Introduction to `ELSE` statement
น้องๆอาจจะสงสัยว่า ถ้าทำแบบนี้ไม่ได้ ก็ทำแบบนี้แทนได้มั้ย ตัว Statement ELSE ก็มาช่วยน้องแล้วจ้า

> Else Statement จะต้องใช้กับ If statement ทุกครั้ง

ตัวอย่างการใช้งาน else
```python
if (kumamon == "Cute"):
    print("Cute Kumamon")
else:
    print("I don't understand")
```
น้องจะเห็นว่า การเขียน else นั้นจะทำการเขียนไว้หลัง if statement และ else ก็จะไม่มีสมการเพื่อมาทดสอบ logic (kumamon == "Cute") อยู่ **เพราะว่า else จะทำงานทันที หากว่า if ไม่ทำงาน**

แล้วถ้าน้องเจอโจทย์แบบนี้หล่ะ<br>
หากว่า kumamon = "Cute" ก็ให้ออก "Cute Kumamon"<br>
หากว่า kumamon = "Happy" ก็ให้ออก "Happy Kumamon"<br>
หากว่า kumamon = "Funny" ก็ให้ออก "Funny Kumamon"<br>
แต่ถ้าไม่เหมือนอะไรเลย ก็ให้ออก "I don't understand"

น้องก็สามารถเขียนภาษา Python ได้ดังนี้
```python
if (kumamon == "Cute"):
    print("Cute Kumamon")
else:
    if (kumamon == "Happy"):
        print("Happy Kumamon")
    else:
        if (kumamon == "Funny"):
            print("Funny Kumamon")
        else:
            print("I don't understand")
```
แต่ มัน อ่าน ไม่ ออก โหวยยยยยยยยย ไม่เอา ไม่เขียนแบบนี้

น้องก็สามารถใช้ `elif` ได้ครับ

## Introduction to `ELIF` statement
เนื่องจากว่าคนสร้าง Python เค้าคงรำคาณตายเลย ถ้าจะเขียน if else if else เยอะแยะ น้องก็สามารถใช้ `elif` มาทดแทนโค้ด้านบนได้ดังนี้
```python
if (kumamon == "Cute"):
    print("Hello World")
elif (kumamon == "Hello Kumamon"):
    print("Go straight to jail")
else:
    print("I don't understand")
```

น้องๆต้องสังเกตุ Indentation ด้วยนะครับ ว่ามันอยู่บรรทัดเดียวกันกับ if และ else เลย เพราะหากว่าถ้า if ไม่เป็นจริง ก็จะลอง elif อันต่อไปทันที

## Nested Statement
เนื่องน้องได้ลองเขียนไปแล้วเนอะ วิธีการเขียน If กับ Else statement

แต่ถ้าน้องเจอโจทย์แบบนี้หล่ะ
![](https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fdatabricks.com%2Fwp-content%2Fuploads%2F2014%2F09%2Fdecision-tree-example.png&f=1)<br>
โดยหากว่า ตัวแปร weight เท่ากับ ตัวแปร heavy ก็ให้ออกผลลัพท์ "High Milleage" แต่ถ้าไม่ใช่ ก็ให้ทำการเช็คว่าตัวแปร horsepower นั้นมีค่าน้อยกว่าหรือเท่ากับ 86 หรือไม่ หากใช่ก็ให้ทำการออกว่า "High Mileage" แต่ถ้าไม่ใช่ ก็ให้ออก "Low Milleage"

น้องลองเขียนโปรแกรมดูก่อนนะครับ ก่อนดูเฉลยวิธีการเขียน

แอบดูคำตอบแล้วยังไม่ได้เขียนเหรอ เห้ออออออ
```python
if (weight = heavy):
    print("High Milleage")
elif (horsepower <= 86):
    print("High Milleage")
else:
    print("Low Milleage")
```

หรือน้องจะเขียนแบบนี้ก็ได้ครับ
```python
if (weight = heavy || horsepower <= 86):
    print("High Milleage")
else:
    print("Low Milleage")
```

หรือน้องจะเขียนแบบนี้ก็ได้ครับ
```python
if (weight = heavy):
    print("High Milleage")
else:
    if (horsepower <= 86):
        print("High Milleage")
    else:
        print("Low Milleage")
```

---
::: tip Terminology
[`Logic`][1]
[`Statement`][2]

[1]: https://en.wikipedia.org/wiki/Logic_in_computer_science
[2]: https://en.wikipedia.org/wiki/Statement_(computer_science)
:::

<h5 text-align:cemnter
