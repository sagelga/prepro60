# Introduction to Python
สวัสดีครับ พี่ชื่อพี่คุมะมง วันนี้พี่จะมาสอนน้องเขียนโปรแกรมตั้งแต่ลง Python ยันเขียนโปรแกรมสวัสดีชาวโลกเลยนะครับ

## What is Python
น้องอาจจะยังสงสัย ว่ามันคืออะไรอ่ะ Python

Python เป็นภาษาคอมพิวเตอร์ที่ให้น้องสามารถกำหนดว่าให้คอมพิวเตอร์มันทำอะไรบ้าง ซึ่งการเรียนที่คณะ IT และวิชา Problem Solving in IT นี้ เราใช้ Python เพราะว่ามันเข้าใจง่าย และน้องก็ "ไม่ต้องเสียเวลา" เพื่อมาแก้บัคอะไรให้มากมาย เพราะอ่านง่าย อิอิ

และ Python นั้นเป็นภาษาที่รองรับระบบปฎิบัติการเยอะแยะไปหมด ทำให้มันแพร่หลาย และถูกนำไปใช้งานในหลายๆวิธีเลย

## Installing Python
ก่อนที่น้องๆจะเล่นและเขียนโปรแกรมไปกับ Python เนี่ย น้องๆจะต้อง download + install Python ซะก่อนครับ

::: warning
ถ้าน้องๆใช้ MacOS หรือ Linux หรือน้องไม่รู้ว่ามี Python อยู่ที่เครื่องหรือเปล่า อาจจะข้ามไปอ่านขั้นตอนต่อไปก่อนก็ได้นะครับ

สำหรับน้องๆที่ใช้ Windows ถ้าไม่มี IDLE ก็ download + install Python เถอะครับ
:::

### Downloading Python
โดยเราจะใช้เวอร์ชั่นของ Python เป็นเวอร์ชั่น 3 นะครับ (ไม่ใช่ 2)

น้องๆสามารถดาวน์โหลดตัว Python + Python IDE (IDLE) ได้ที่เว็บไซต์ของ Python.org ได้เลยครับ

ดาวน์โหลดได้ที่นี่ครับ [https://www.python.org/downloads/](https://www.python.org/downloads/)

โดยให้น้องดาวน์โหลดเวอร์ชันล่าสุด โดยเวอร์ชั่นล่าสุดจะปุ่มสีเหลืองตามภาพก็ให้กดเพื่อดาวน์โหลด Python ลงเครื่องของน้องๆครับ

![](https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fopensourceforu.com%2Fwp-content%2Fuploads%2F2016%2F09%2FFigure-1-Python-download-page-from-the-official-portal.jpg&f=1)<br>
ตามภาพ น้องจะเห็นได้ว่าปุ่มดาวน์โหลด Python เป็น version 3.5.2 <br>
**ดังนั้น น้องก็ไปกดปุ่มสีเหลืองเพื่อดาวน์โหลดนะครับ (รู้สึกว่าจะเขียนเป็นเวอร์ชั่น 3.6.2 แล้ว)**

แล้วก็กด install มันครับ และก็กด Next ยาวๆไป

หรือสำหรับน้องๆที่อยากท้าทายตัวเอง และอยากใช้ Python บน command line<br>
น้องๆที่ใช้ MacOS สามารถพิมพ์
```
# หากน้องยังไม่มี Homebrew บนเครื่อง ก็ให้พิพม์บรรทัดด้านล่างไปด้วยนะครับ
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# อันนี้เอาไว้ดาวน์โหลด Python3 ลงเครื่อง (ต้องมี Homebrew ก่อนนะครับ)
brew install python3
```

## Is Python in your computer?
สำหรับน้องที่ใช้ MacOS หรือ Linux Distributions ทั้งหลาย สามารถเช็คว่ามี Python ในเครื่องแล้วหรือยัง โดยการพิพม์
```
python3
```

และสำหรับน้องๆที่ใช้ Windows ถ้าเห็น IDLE อยู่บน desktop (หรือที่น้องเก็บมันไว้) ก็ถือว่าดาวน์โหลดเรียบร้อยแล้วครับ

## Welcome to IDLE
::: warning
สำหรับน้องที่ดาวน์โหลด Python มาจากเว็บไซต์ และดาวน์โหลด IDLE มาด้วยเท่านั้นนะครับ
:::

IDLE คือตัว Text Editor ของ Python เอง ซึ่งมันก็จะแตกต่างกับตัว Text Editor อื่นๆ (เช่น Atom, Sublime Text, VS Code) นั่นก็คือมันใช้งานง่ายกว่า และก็สามารถกด `F5` เพื่อทำการรันโปรแกรมได้เลย (สำหรับน้องๆที่ใช้ Windows)

โดยเปิดตัว IDLE ขึ้นมาแล้ว น้องๆก็จะเห็นหน้าต่างที่หน้าตาเหมือน command line / shell (ตามภาพ)

![](https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fi.stack.imgur.com%2Fbz1qE.jpg&f=1)<br>
หน้าต่าง Python Shell

## Welcome to Python Shell
::: warning
สำหรับน้องที่ดาวน์โหลด Python มาโดยการใช้ Homebrew หรือมีบนเครื่องแล้ว
:::

ตัว Python บน command line ก็สามารถเรียกได้โดยการพิพม์
```
python3
```
และหน้าจอของน้องๆก็จะเป็นดังภาพ

หรือน้องๆที่ใช้ Windows ก็สามารถเขียนภาษา Python โดยใช้ shell ได้เหมือนกัน โดยการกดเข้าโปรแกรม Python Shell ก็จะได้ผลลัพท์เช่นเดียวกัน

![](https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fraphaelmarques.files.wordpress.com%2F2010%2F03%2Fterminal-python.png&f=1)

## Playing with Python
ใน lecture นี้ พี่มงจะสอนวิธีทั่วๆไปก่อนเนอะ เช่นสวัสดีชาวโลกให้หน่อย อะไรแบบนี้<br>
พี่จะให้น้องสร้างไฟล์ Python (.py) และเอาไฟล์นั้นไปรันนะครับ

ขั้นตอนแรกให้น้องสร้างไฟล์ใหม่ก่อน โดยการกด File -> New File และน้องๆก็จะเห็นหน้าต่างนี้ขึ้นมา

![](https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.w3resource.com%2Fw3r_images%2Fpython-idle-new-window.png&f=1)<br>
ภาพด้านบนเป็นหน้าต่างเขียนโปรแกรม Python น้องสามารถเขียนโปรแกรม Python ในนั้นได้เลยครับ

และก็ให้น้องๆลองพิมพ์ 
``` python
print("Hello World")
```
ในหน้า Text Editor ของ IDLE และน้องก็กดเซฟไฟล์ (Ctrl + S สำหรับ Windows และ Cmd + S สำหรับ MacOS + Linux)

และก็เข้าตรงแท็บที่เขียนว่า "Run" และกด "Run Module" (หรือกด F5 สำหรับน้องๆที่ใช้ Windows) เพื่อรันโปรแกรมนะครับ

น้องก็จะเห็นว่า Python เขียนอะไรกลับมา

::: tip
สำหรับน้องๆที่ยังไม่เข้าใจว่า `print()` คืออะไร มันก็คือวิธีการแสดงผลลัพท์บนหน้าจอให้น้องนั่นเอง
:::

ง่ายใช่มั้ยหล่ะ อิอิ

---
<center>Created by P'Kumamon IT14</center>



