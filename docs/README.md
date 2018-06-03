# What is EJudge?

ระบบ Ejudge เป็นระบบ Grader ชนิดหนึ่ง ที่จะรับโปรแกรมของน้องๆมา แล้วรัน โดยการใส่ค่า Input ที่พวกพี่ๆที่ออกโจทย์เขียนเอาไว้ + รับค่า Output ที่ผ่านโปรแกรมนั้นๆออกมา
โดยระบบจะเช็คได้ถึง

1. **ความมีระเบียบ** ในการเขียนโปรแกรม (คุณภาพ)

2. **ความคล้ายคลึงใน Algorithm** ในโปรแกรมน้องๆ กับเพี่อนของน้องๆ

3. **ความถูกต้องในผลลัพท์** ที่ออกมาจากโปรแกรมที่น้องๆเขียนมา

4. **เก็บคะแนน** และเก็บไฟล์ที่น้องเคยส่งมาทั้งหมด


โดยน้องๆก็จะเจอกับระบบนี้ไปอีกนาน เพราะน้องต้องเรียนกับมัน สอบกับมัน ทำ Quiz กับมัน ดังนั้น ก็ให้เข้าใจและชินไปกับระบบครับ


วิธีระบบ Ejudge คำนวณคะแนน
หากน้องทำได้เพียง 9 ใน 10 testcase ได้ถูกต้อง และคะแนนต่อข้อ = 100 คะแนน และระดับความยาก = 5 และ ทำคุณภาพ code ระดับไม่มีที่ติ


|Testcase Score|Difficulty|Perfect bonus score|Quality|Total|
|--------------|----------|-------------------|-------|-----|
|(9/10) x 100  |x5        |100 x 5 x 0        |100%   |90 x 5 x 1 + 0 = 450|


หากน้องทำได้ 10 ใน 10 testcase ได้ถูกต้อง และคะแนนต่อข้อ = 100 คะแนน
และระดับความยาก = 5 และ ทำคุณภาพ code ระดับไม่มีที่ติ

|Testcase Score|Difficulty|Perfect bonus score|Quality|Total|
|--------------|----------|-------------------|-------|-----|
|(10/10) x 100 |	      x5|100 x 5 x 2        |100%   |100 x 5 x 1 + 500 = 1000|


เห็นความแตกต่างนั่นมั้ยเอ่ย? 450 กับ 1000 คะแนน? Welcome to the PSIT.
________________

# เนื้อหาการเรียนอย่างคร่าวๆ
### 1 Introduction to Python
What is Python? / Why Python? / Python Coding Modes and Compatibility

### 2 Variable expressions, statements and elementally Input / Output
One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value.

### 3 Function
A function is a group of statements that together perform a task.

### 4 Strings
A string is a sequence, which means it is an ordered collection of other values. In this chapter you’ll see how to access the characters that make up a string, and you’ll learn about some of the methods strings provide.

### 5 Decision Flow
The main topic of this chapter is the if statement, which executes different code depending on the state of the program

### 6 Iteration For / While
This chapter is about iteration, which is the ability to run a block of statements repeatedly.

### 7 List, Tuple
This chapter presents one of Python’s most useful built-in types, lists. You will also learn more about objects and what can happen when you have more than one name for the same object.

### 8 Dict, Set
Dictionaries are one of Python’s best features; they are the building blocks of many efficient and elegant algorithms.

Set is one of Python’s data structure. It’s the same as Set that we learned in Grade 10.

**สำหรับน้องที่อยากเรียนล่วงหน้า พี่และอาจารย์โชใช้หนังสือ Think Python เป็น Reference ครับ**
________________

# Why Python?
น้องอาจจะไม่เข้าใจ ว่าทำไม เราต้องมาเรียน Python ด้วย ทำไมไม่เรียน C/Java ก่อน หรือ ไม่เรียน Ruby หรือ Swift ก่อน เพื่อเป็นการเรียนวิธีคิด พี่อยากจะบอกข้อดีของ Python ให้น้องฟังครับ

- **Speed** น้องเขียนภาษานี้ ได้เร็ว (เพราะเป็นภาษา High Level)

- **Integrations** ระบบต่างๆ นั้นรองรับภาษา Python ทั้งหมด หากไม่รองรับ ก็สามารถใช้ Library เพื่อให้มันรองรับได้

- **Compatibility** ใช้ได้กับทุก platform หลักๆ เช่น Windows (.NET) และ UNIX (MacOS & Linux Distribution & Android)

---

# Before Coding
ก่อนน้องจะเข้ามาเรียน Online พี่แนะนำให้น้องทำพวกนี้ก่อนครับ
ใช้ + เลือก IDE และ Text Editor ที่เหมาะกับตัวน้องเองมากที่สุด
(เพราะมันจะอยู่กับตัวน้องตลอดไป

โดยโปรแกรมที่มีติดไว้กับเครื่องคอมพิวเตอร์ห้องสอบนั้มีเพียง Sublime Text, Atom, Visual Studio, NotePad และ Python IDE (IDLE) ครับ หากสะดวกใช้อันไหนก็ใช้ไปครับ

---

# ของฟรีที่น้องจะได้จากการเป็นนักศึกษา ITKMITL
ผู้ใหญ่ใจดีแจก

1. **Microsoft Office 365 5 ปีเต็ม** รวมทั้ง Microsoft Word, Excel, PowerPoint, Outlook และอื่นๆ เช่นเดียวกันกับ OneDrive ที่มีให้ถึง 1TB

2. **Microsoft Windows 10 Education** ใช้งานได้เหมือนกับ Windows 10 ปกติเลย แค่ฟรีเท่านั้นเอง

3. **Azure $100 Free Credit**

4. **Unlimited Private Repository** ใช้ฟรีตลอดไปครับ (แต่ต้องไปต่ออายุทุกปีเท่านั้นเอง)

5. **GitHub Student Pack** เข้าไปอ่านครับ ว่าได้อะไรจาก Student Pack นะ

6. **Google Education Accounts** เป็นอีเมล์ @it.kmitl.ac.th และ @kmitl.ac.th ให้น้องๆเก็บไว้ดูเล่นตลอดชีวิต รวมทั้งการเก็บไฟล์ Google Drive อย่างไม่จำกัด (อีเมล์จะไม่ถูกปิดหลังน้องจบไปแล้ว น้องก็สามารถใช้ไปยาวๆเลย)

7. **JetBrains Product**

8. **AWS $150 Free Credit** + Free Tier มันแจกฟรีครับ เปิด Server ได้ยาวๆ 1 ปีเต็ม ไม่ต้องปิดเลย

________________

# การเรียน และ การสอบวิชา PSIT
สำหรับการเรียน วิชาเขียนโปรแกรม ไม่ว่าจะเป็น ภาษา Python, C, Java จะมีความความคล้ายคลึงกันอยู่บ้าง แต่ตอนนี้ พี่คุมะมงจะเล่าก่อน ว่าจะเกิดอะไรขื้นในวิชา Python

อาจารย์โชติพัฒน์นั้นเป็นคนใจดีครับ และก็จะมีการเรียนคาบ Lecture (ทฤษฎี) และ คาบ Lab (ปฏิบัติ) ซื่งเนื่อหาคาบ Lab จะมาจาก Lecture ซะส่วนใหญ่

ตอนนี้น้องๆรู้แค่สี่งที่ทำได้ กับไม่ได้ดีกว่าเนอะ

# โปรแกรมที่สามารถใช้ได้ในห้องสอบ
ในห้องสอบ PSIT นั้่น น้องก็จะได้ใช้คอมพิวเตอร์ PC (ซึ่งทำใมตอนเรียน แล้วใช้ macOS หล่ะนั่น) โดยที่เครื่องคอมพิวเตอร์จะปิดเน็ด ปิดการเชื่อมต่อกับอินเตอร์เน็ด เหลือเพียงเว็บ Ejudge ที่ยังสามารถเข้าไปส่งคำตอบของน้องได้

น้องสามารถเตรียมของพวกนี้เข้าไปได้ด้วย
- **ดินสอ ปากกา** (ปากกาต้องเอามา) เพื่อจะทด(หากต้องทด) และเซ็นต์ชื่อเข้าสอบ
- **บัตรประจำตัวนักศึกษา** ต้องมี ถ้าไม่มีจะไม่สามารถเข้าห้องสอบได้ (หากลืมหรือหายจริงๆ สามารถติดต่อสำนักทะเบียน (ของมหาลัย) เพื่อออกใบเข้าสอบได้ครับ)
- **ขนม (ประเภทอม)** (ปีของพี่เอาเข้าได้) โดยจะต้องเป็นขนมที่ไม่ทำให้คนสอบรอบข้างไม่หิวไปด้วย และไม่รบกวนคนอื่น

# ฟังก์ชั่นบน Ejudge ที่จะถูกปิดไป
1. คะแนนของเพื่อนๆ และของตัวเอง แต่ยังสามารถดูได้ว่าข้อนี้มีคนส่งไปแล้วกี่คน

2. เกจ Quality โดยที่จะบอกเพียงว่า อยู่ประมาณไหน จะไม่รู้เลยว่าโดนหักคะแนนไปมากขนาดไหน แต่จะยังบอกเป็นเพียงลางๆเท่านั้น เช่น 75% - 100% หรีือ 50% - 75%

3. ระบบ Code Simulator เนื่องจากอินเตอร์เน็ดจากภายนอกจะถูกปิดทั้งหมด

________________

# FAQ
Q : น้องเรียนสาขา Data Sci อ่ะครับ ทำไมน้องต้องมาเรียนกับสาขา IT ด้วย

A : น้องที่เรียนสาขา Data Sci ก็จะได้เรียนวิชาที่แตกต่างกับน้องๆ IT เหมือนกัน แต่จะมีภาษาโปรแกรม ที่น้องต้องใช้เหมือนกัน คือ Python ครับ
รู้จักการ Data Analysis หรือเปล่า พวกนั้น เราก็ใช้ Python ในการเขียนจำลองนะ (พวกนั้นคือ Modules ครับ ตัว Python มีเยอะมากเลย พี่ๆก็นับไมไหวหรอก แต่มีที่เด่นชัดคือ

---

Q : พี่มงครับ เรียน PreProgramming ไปแล้ว ได้คะแนนจิตวิสัยวิชา PSIT หรือเปล่าครับ

A : การเรียน Pre Programming บ่งบอกถึงความรู้ Python ของน้องๆ ว่าน้องพร้อมที่จะไปเรียน PSIT มากขนาดไหนแล้วเท่านั้นเอง

---

Q : พี่มงครับ เรียน Pre Programming ไปทำไมเหรอ

A : การเรียน Pre Programming เป็นกิจกรรมฝึกน้องๆเขียน Python ให้เป็น เพี่อไปทำโจทย์เขียนโปรแกรมในอนาคตครับ

---

Q : พี่มงครับ ถ้าผมทำทุกข้อ พี่การันตีเกรดผมหรือเปล่า

A : อันนี้พี่การันตีไม่ได้แน่นอนครับ แต่ความเป็นไปได้ว่า ถ้าน้องทำได้ทุกข้อ Mid Term ของน้องๆก็จะสบายขื้นเยอะครับ มีสิทธิได้ B, B+, A สูงครับ

---

Q : พี่มงครับ ผมว่าผมชอบภาษา C / JAVA มากกว่า Python อ่ะครับ

A : พี่เข้าใจครับ แต่ว่าการเรียน Python เป็นการฝึกเขียนโปรแกรมอย่างพื้นฐานจริงๆนะครับ

---

Q : พี่มงครับ ทำไมอาจารย์งกเกรด A จังเลยครับ

A : เค้ามีเหตุผลของเค้าครับ อาจารย์ทุกคนจะมีเกรดเฉลี่ยกลาง (เกรดเฉลี่ยของน้องๆทุกคนในวิชานั้นๆ) ไม่เท่ากัน โดยที่เค้าห้ามตัดเกรดเกินค่ากลางนั้นครับ พวก A คือคะแนนพวกเขาโดดมาก เลยได้เกรด A ครับ

---

# Reference
### Think Python v.2 :
![](http://greenteapress.com/thinkpython/think_python_comp2.medium.png)

http://greenteapress.com/thinkpython2/thinkpython2.pdf

เป็นหนังสือที่อาจารย์โชบอกว่ามันดีครับ (มัน Creative Commons อ่ะครับ เออ มันดี)

ขอเตือนนะครับ อาจารย์เค้าความจำดีครับ น้องเล่นอะไรแผลงๆ เค้าจำได้นะครับ พี่ต้องขอเตือนไว้ก่อน อิอิ

## Follow me on GitHub
|<a href="https://github.com/sagelga"><img src="https://avatars0.githubusercontent.com/u/13056824" width="100px"></a>  |
|:-:|  
|@sagelga|

Copyright by P' Kumamon IT14. <br>
For education purpose only.

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)
