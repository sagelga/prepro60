# กำหนดการ Pre-Programming by P’ Kumamon

|ต้นเดือน 4|เดือน 7|ก่อนเป็นปี 1|เป็นปี 1 แล้ว|
|---------|------|---------|---------|
|Pre Programming รอบ Online|Pre Programming รอบ On-Site|First Day + Registration|กิจกรรมของคณะ|
|[[1]](https://github.com/sagelga/PreProgramming-60/edit/master/Activity%20Schedule%20IT15.md)|[[2]](https://github.com/sagelga/PreProgramming-60/blob/master/Activity%20Schedule%20IT15.md#เดือน-7-8)|[[3]](https://github.com/sagelga/PreProgramming-60/blob/master/Activity%20Schedule%20IT15.md#เดือน-8-น้องเกือบเป็นนักศึกษาแล้ว)|[[4]](https://github.com/sagelga/PreProgramming-60/blob/master/Activity%20Schedule%20IT15.md#เดือน-8-12-น้องเป็นนักศึกษาปี-1-เต็มตัว)|

# What is EJudge?

![](https://www.dropbox.com/s/vk2ir2900lv4jti/EJudge.png?raw=1)

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

# เนื้อหาการเรียนรอบ Online อย่างคร่าวๆ
### 0	Creation of Website + Website Hosting on AWS
by P’ Dobakung + P’ Kumamon

Syntax for HTML + CSS / Hosting Website on AWS services

### 1 Introduction to Python
by P’ Dem

What is Python? / Why Python? / Python Coding Modes and Compatibility

### 2 Variable expressions, statements and elementally Input / Output
by P’ Bank

One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value.

### 3 Function
by P’ Foo

A function is a group of statements that together perform a task.

### 4 Strings
by P’ Boon

A string is a sequence, which means it is an ordered collection of other values. In this chapter you’ll see how to access the characters that make up a string, and you’ll learn about some of the methods strings provide.

### 5 Decision Flow
by P’ Koung

The main topic of this chapter is the if statement, which executes different code depending on the state of the program

### 6 Iteration For / While
by P’ Start

This chapter is about iteration, which is the ability to run a block of statements repeatedly.

### 7 List, Tuple
by P’ Sky & P’ Top

This chapter presents one of Python’s most useful built-in types, lists. You will also learn more about objects and what can happen when you have more than one name for the same object.

### 8 Dict, Set
by P’ Tom

Dictionaries are one of Python’s best features; they are the building blocks of many efficient and elegant algorithms.

Set is one of Python’s data structure. It’s the same as Set that we learned in Grade 10.

**สำหรับน้องที่อยากเรียนล่วงหน้า พี่และอาจารย์โชใช้หนังสือ Think Python เป็น Reference ครับ**
________________
# Why Python?
น้องอาจจะไม่เข้าใจ ว่าทำไม เราต้องมาเรียน Python ด้วย ทำไมไม่เรียน C/Java ก่อน หรือ ไม่เรียน Ruby หรือ Swift ก่อน เพื่อเป็นการเรียนวิธีคิด พี่อยากจะบอกข้อดีของ Python ให้น้องฟังครับ

- **Speed** น้องเขียนภาษานี้ ได้เร็ว (เพราะเป็นภาษา High Level)

- **Integrations** ระบบต่างๆ นั้นรองรับภาษา Python ทั้งหมด หากไม่รองรับ ก็สามารถใช้ Library เพื่อให้มันรองรับได้

- **Compatibility** ใช้ได้กับทุก platform หลักๆ เช่น Windows (.NET) และ UNIX (MacOS & Linux Distribution & Android)
________________
# Before Coding
ก่อนน้องจะเข้ามาเรียน Online พี่แนะนำให้น้องทำพวกนี้ก่อนครับ
ใช้ + เลือก IDE และ Text Editor ที่เหมาะกับตัวน้องเองมากที่สุด
(เพราะมันจะอยู่กับตัวน้องตลอดไป

โดยโปรแกรมที่มีติดไว้กับเครื่องคอมพิวเตอร์ห้องสอบนั้มีเพียง Sublime Text, Atom, Visual Studio, NotePad และ Python IDE (IDLE) ครับ หากสะดวกใช้อันไหนก็ใช้ไปครับ

________________

# เดือน 7-8
เรียนรอบ On-Site กับพวกพี่ๆ จะต้องมีอะไรพวกนี้นะครับ

## ซื้อเครื่องแต่งกาย
ตารางเวลาที่จะขาย: <br> โดยน้องควรจะมาซื้อ/จองดังนี้

|รอบที่ 1|รอบที่ 2|
|------|-------|
|จองเสื้อ/กางเกง/กระโปรง <br> (ซื้อร้านข้างนอกก็ได้ครับ มีเยอะแยะอยู่เหมือนกัน บางร้านอาจจะถูกกว่า / แข็งแรงกว่าที่ขายที่นี่นะครับ) <br><br> ซื้อเข็มขัดของผู้ชาย/ผู้หญิง  <br> (อันนี้ไม่มีขายนอกมหาลัยนะจ๊ะ มีทุกไซส์) |รับเสื้อ/กางเกง/กระโปรง ที่จองไว้ตั้งแต่รอบแรก <br><br> ซื้อเข็มขัดของผู้ชาย/ผู้หญิง|

สำหรับเข็มและกระโปรง [กดที่นี่เลยจ้า](https://github.com/sagelga/PreProgramming-60/blob/master/Activity%20Schedule%20IT15.md#เดือน-8-12-น้องเป็นนักศึกษาปี-1-เต็มตัว)

________________

## เรียน Onsite
การเรียน Onsite นี้จะแตกต่างกับรอบ Online ในระดับหนึ่ง เพราะจะเป็นการรีวิวข้อสอบ หรือแนวข้อสอบ เพื่อจะให้น้องๆไปสอบได้อย่างสบายใจ ได้คะแนนกันพุ่งพรวดเลยทีเดียว (อิอิ) แต่สำหรรับน้องรอบ Admission นั้น ไม่ต้องกลัวครับ เดี๋ยวพี่ๆจะมาสอนน้องๆ ให้ทันตามเพื่อนๆนะจ๊ะ

โดยหากมีข้อสงสัย หรือ ต้องการความช่วยเหลือ ติดต่อพี่ๆประจำห้องได้เลยนะครับ

## หาที่อยู่ (หอพัก)
หอพัก พี่มงก็ไม่ค่อยจะรู้เรื่องเท่าไหร่จ้า เช่นว่าสี่งอำนวยความสะดวก เอาเป็นว่า เสริจ Google Maps แล้วไปลองดูจริงๆก่อนที่น้องจะเลือกดูก็ได้จ้า โดยจะมีโซนหลักๆคือ
1. เกกี (อยู่แถวนี้ https://goo.gl/maps/pX5ARMGMNZ62)
2. หอพักของมหาลัย https://goo.gl/maps/kaqZHBVJKYB2
3. หน้ามหาลัย (อยู่แถวนี้ https://goo.gl/maps/NdyzVqv88iw)
4. ถนนฉลองกรุง (อยู่แถวนี้ https://goo.gl/maps/iSWHjzZ3Hyx)

## การเดินทางระหว่างมหาลัยและบ้าน
ตอนนี่ที่พี่คิดออก ก็มีดังนี้ครับ

### ลาดกระบัง -> Seacon Square (ศรีนครินทร์) สามารถกลับบ้านได้ดังนี้
1. นั่งรถ 2 แถว (ที่เขียนว่าไป Airport Link) 7 บาท -> นั่ง Airport Link จากสถานนีลาดกระบัง ไป 2 สถานี ไปลงสถานนีหัวหมาก -> นั่งรถเมล์ป้ายที่ผ่าน Seacon Square หรือหากน้องจะไปไกลกว่านี้ (เช่นปากน้ำ) ก็สามารถนั่งรถเมล์หรือรถตู้ไปก็ได้ครับ
2. นั่งรถ 2 แถวจากฝั่งคณะครุ มาลงหน้าโรงพยาบาลลาดกระบัง -> เดืนไปขื้นรถตู้ไป Seacon Square ในฝั่งตรงข้าม

บ้านน้องอยู่ไหน ลองบอกพี่ดูครับ เดี๋ยวพี่จะลองคิดเส้นทางให้นะจ๊ะ
________________

# เดือน 8 (น้องเกือบเป็นนักศึกษาแล้ว)
สำหรับกิจกรรมที่พี่เขียนข้างต้น พี่ๆปี 2 จะเป็นคนช่วยเหลือน้องๆ ตลอดครับ ดังนั้น ก็ลองฟังก่อน ว่าก่อนที่น้องจะได้มาเป็น ปี 1 อย่างสมใจอยาก นั้นต้องทำอะไรก่อนบ้าง

1. กิจกรรม First Day (เค้าจะเรียกว่า รับน้องรถไฟครับ) อันนี้ เป็นกิจกรรมตามความสมัครใจครับ สถาบันไม่บังคับให้ไม่เข้าร่วมกิจกรรมใดๆทั้งสี้นอยู่แล้วนะครับ ตามความสมัครใจของน้องๆเพียงผู้เดียว

2. ยื่นข้อมูลเอกสารน้องๆให้สถาบัน (รายงานตัว) เพื่อเข้าสู่รั้วมหาลัยอย่างแท้จริง โดยสำหรับข้อมูล ต้องเอาอะไรไปบ้าง และเวลาไหน ที่ไหน ให้ดูในตารางการรายงานตัวนะครับ http://www.reg.kmitl.ac.th/educalendar/index.php

ที่หลักๆ ก็จะมีตามเช็คลิสต์นี้ http://www.reg.kmitl.ac.th/directEnt/checkpoint-57/10.pdf

1. เอกสารการตรวจร่างกาย โดยที่ต้องไปโหลดฟอร์มบนเว็บไซต์ reg.kmitl.ac.th
2. ใบ ปพ 1 (จริง 1 ชุด สำเนา 2 ชุด)
3. สำเนาบัตรประชาชน 2 ชุด

โดยทางมหาลัยจะเปิดบัญชี (เพื่อหักค่าเรียน) ให้ และจะประกาศว่าให้ไปเอาช่วงไหน

3. กิจกรรมปฐมนิเทศ (ต้องมาทุกคน เพี่อมาเอารหัสเข้าระบบ Ejudge ของจริง + รู้จักระบบและกฎของมหาลัยเบื้องต้น + ครูผู้ช่วยประจำ section)

________________

# เดือน 8-12 (น้องเป็นนักศึกษาปี 1 เต็มตัว)
กิจกรรมพวกนี้ น้องๆจะเป็นคนดูแล 90% ส่วนอีกเล็กน้อย คือพี่ๆมาช่วยน้องๆครับ โดยเดี๋ยวใกล้ๆแล้ว พวกพี่ะจะมาเตือนน้องๆอีกรอบนะครับ

1. กิจกรรมติดไทต์ (สำหรับ ผช) + เข็ม (สำหรับ ผญ) เป็นการรับน้องเข้าสู่ชาวลาดกระบังอย่างเต็มภาคภูมิ (หากน้องไม่มา ต้องไปหาซื้อเอาเองนะครับ สำหรับน้องที่เข้างานจะได้รับแจกฟรี) โดยจะมีทั้งหมด 1 รอบเท่านั้น (รอบจริง) แต่น้องควรมาฝึกร้องเพลงของลาดกระบัง และ ฝึกว่าน้องควรทำอะไรระหว่างงานด้วยนะครับ (รอบซ้อม)

2. Open House และงานในระดับคณะ (ประมาณ 3-4 งานนะครับ) ที่รุ่นน้องๆต้องรับผิดชอบเอง แต่จะมีรุ่นพี่ มาแนะนำ ว่าทำยังไง หรือมาช่วยงานน้องๆได้บ้่าง <br> โดยเรื่อง Open House นี้ น้องส่วนใหญ่จะได้เป็นผู้ช่วยงานมากกว่าคนรันงาน (หัวหน้างาน) เนื่องจากว่ามันยากจ้า อิอิ

3. หา หัวหน้ารุ่น รองหัวหน้ารุ่น หัวหน้าการเก็บเงินรุ่นเอง กิจกรรมต้องใช้เงินรุ่นซะส่วนใหญ่ครับ (รุ่นของพี่มง IT14 เก็บคนละ 100 บาทต่อเดือนต่อคน ก็ยังไม่พอนะจ๊ะ งานที่ต้องใช้งบประมาณรุ่น เยอะอยู่เหมือนกัน)

4. พี่น้องสายรหัส (ดูได้จากข้างล่างครับ ว่ารหัสน้องคืออะไร)

5. กิจกรรมกีฬา และ Cheerleader ระดับในคณะ เป็นตัวแทนกลุ่มของเพื่อนๆ / ระดับมหาลัย เป็นตัวแทนคณะ IT / ระดับ IT เจ้าคุณทหาร (KMITL + KMUTT + KMUTNB) เป็นตัวแทนคณะ IT ต่อมหาลัยในเครือเจ้าคุณทหาร

6. ทำบัตรนักศึกษา (น่าจะเป็นบัตรเดบิต + บัตรนักศึกษา) โดยจะมีการบอกอีกครั้งหนึ่ง
________________

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
_______________
Q : พี่มงครับ เรียน PreProgramming ไปแล้ว ได้คะแนนจิตวิสัยวิชา PSIT หรือเปล่าครับ

A : มันไม่มีหรอกครับ คะแนนพวกนั้น แต่การเรียน Pre Programming บ่งบอกถึงความรู้ Python ของน้องๆ ว่าน้องพร้อมที่จะไปเรียน PSIT มากขนาดไหนแล้วเท่านั้นเอง
________________
Q : พี่มงครับ เรียน Pre Programming ไปทำไมเหรอ

A : การเรียน Pre Programming เป็นกิจกรรมเชิงชักชวน ไม่ได้เป็นการบังคับ หรือเป็นส่วนหนึ่งของวิชาใดๆในคณะ แต่เป็นแค่การฝึกน้องๆเขียน Python ให้เป็น เพี่อไปทำโจทย์เขียนโปรแกรมในอนาคตครับ
________________
Q : พี่มงครับ ถ้าผมทำทุกข้อ พี่การันตีเกรดผมหรือเปล่า

A : อันนี้พี่การันตีไม่ได้แน่นอนครับ แต่ความเป็นไปได้ว่า ถ้าน้องทำได้ทุกข้อ Mid Term ของน้องๆก็จะสบายขื้นเยอะครับ มีสิทธิได้ B, B+, A สูงครับ
________________
Q : พี่มงครับ ผมว่าผมชอบภาษา C / JAVA มากกว่า Python อ่ะครับ

A : พี่เข้าใจครับ แต่ว่าการเรียน Python เป็นการฝึกเขียนโปรแกรมอย่างพื้นฐานจริงๆนะครับ
________________
Q : พี่มงครับ ทำไมอาจารย์งกเกรด A จังเลยครับ

A : เค้ามีเหตุผลของเค้าครับ อาจารย์ทุกคนจะมีเกรดเฉลี่ยกลาง (เกรดเฉลี่ยของน้องๆทุกคนในวิชานั้นๆ) ไม่เท่ากัน โดยที่เค้าห้ามตัดเกรดเกินค่ากลางนั้นครับ พวก A คือคะแนนพวกเขาโดดมาก เลยได้เกรด A ครับ
________________
# Reference
### Think Python v.2 :
![](http://greenteapress.com/thinkpython/think_python_comp2.medium.png)

http://greenteapress.com/thinkpython2/thinkpython2.pdf

เป็นหนังสือที่อาจารย์โชบอกว่ามันดีครับ (มัน Creative Commons อ่ะครับ เออ มันดี)
________________
### This is อาจารย์โช :
![](https://scontent.fbkk12-2.fna.fbcdn.net/v/t1.0-9/14721679_10209523434456073_173788236229106936_n.jpg?oh=335813e3fc0942e42a3f3cab638950ba&oe=59E5EA0E)
https://www.facebook.com/chotipat

ขอเตือนนะครับ อาจารย์เค้าความจำดีครับ น้องเล่นอะไรแผลงๆ เค้าจำได้นะครับ พี่ต้องขอเตือนไว้ก่อน อิอิ

## Follow me on GitHub
|<a href="https://github.com/sagelga"><img src="https://avatars0.githubusercontent.com/u/13056824" width="100px"></a>  |
|:-:|  
|@sagelga|

Copyright by P' Kumamon IT14. <br>
For education purpose only.

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)