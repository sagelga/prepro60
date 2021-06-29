# Week 2 - Plagarism
## Description
![](https://vignette2.wikia.nocookie.net/fallout/images/e/ec/Fo4_Hacker.png/revision/latest?cb=20170320162306)

วันหนี่ง พี่ๆต้องการจะเล่นเกมหนึ่ง ชื่อเกมว่า Fallout 4<br>
ในเกมนั้น พี่ๆจะต้องแฮกคอมพิวเตอร์ โดยที่คอมพิวเตอร์จะแจกรหัสที่จะเข้าคอมพิวเตอร์หลายๆอัน<br>
และให้ผู้เล่นเดารหัส โดยจะมีการใบ้คำตอบให้ ว่าถูกต้องกี่ตำแหน่ง<br>
แต่ทว่า พี่ๆก็อยากจะฝึกให้เก่งๆอ่ะเนอะ มาช่วยพี่ๆที

วันนี้ น้องจึงเป็นคอมพิวเตอร์ ให้เช็คว่าพี่ๆใส่รหัสถูกต้องหรือไม่ โดยให้แสดงจำนวนตัวอักษรที่ถูกต้องเท่านั้น

เช่น<br>
คำตอบที่แท้จริงเพื่อเข้าคอมพิวเตอร์ = 8234<br>
และพี่ๆเดารหัสคอมพิวเตอร์มาว่า = 8542<br>
ซึ่งพี่ๆเดาถูกต้อง 1 ตำแหน่ง (ตัวเลข 8 ในหลักแรก)

ดังนั้น น้องจึงต้องเขียนบอกพี่ๆว่า ถูกต้องไปทั้งหมดกี่ตำแหน่ง<br>
เอาเป็นว่าให้ปรี้นท์อะไร ให้ไปดูใน Output Specification ดีกว่าเนอะ

## Specification
|Input|Output|
|-|-|
|Input x+1 บรรทัด [สูงสุด 21 บรรทัด] (Integer หรือ String) <br> บรรทัดแรก เป็นคำตอบที่ถูกต้อง <br> บรรทัดที่สองเป็นต้นไป เป็นคำตอบที่พี่ๆเดาออกมา <br> และรับมาเรื่อยๆ จนกว่าพี่ๆจะเดาได้ถูกต้อง หรือครบ 20 ครั้ง <br>  <br> โดยค่าที่รับมา หากเป็นตัวอักษร <br> ตัวอักษรตัวใหญ่และเล็กจะถือว่าเป็นตัวเดียวกัน เช่น kuma = KUMA|Output ทุกบรรทัดที่พี่ๆเดา [สูงสุด 20 บรรทัด] (String) <br> หาก เดาได้ถูกหรือไม่ถูกเลย จะให้ตอบว่า Likeness = x (โดย x คือตอบได้ตรงคำตอบกี่ตำแหน่ง) <br>  <br> หาก รหัสที่พี่ๆเดา ความยาวไม่เท่ากับคำตอบ จะให้ตอบว่า Entry Denied <br>  <br> หาก เดาได้ตรงกับคำตอบ จะให้ตอบว่า System Unlocked <br> แทนการปรี้นท์ Likeness หรือ Entry Denied และหยุดการทำงานของโปรแกรมทันที <br>  <br> หาก เป็นการเดาครั้งที่ 20 แล้วยังคงเดาได้ไม่ตรงกับคำตอบ (ยังคงตอบผิด หรือ Entry Denied) <br> จะให้ตอบว่า System Locked Down แทนการปรี้นท์ Likeness หรือ Entry Denied <br> และหยุดการทำงานของโปรแกรมทันที|

## Sample Input / Output
|Input|Output|
|-|-|
|1234 <br> 1000 <br> 0200 <br> 0030 <br> 0004 <br> 1234|Likeness = 1 <br> Likeness = 1 <br> Likeness = 1 <br> Likeness = 1 <br> System Unlocked|
|kumamon <br> kynonan <br> KYNONAN <br> kYnOnAn <br> KUMAMON|Likeness = 2 <br> Likeness = 2 <br> Likeness = 2 <br> System Unlocked|
|1234 <br> 1234567 <br> 123 <br> 12340 <br> ABCD <br> A234 <br> 1234|Entry Denied <br> Entry Denied <br> Entry Denied <br> Likeness = 0 <br> Likeness = 3 <br> System Unlocked|
|12345 <br> 10000 <br> 12000 <br> 12300 <br> 12340 <br> 12345|Likeness = 1 <br> Likeness = 2 <br> Likeness = 3 <br> Likeness = 4 <br> System Unlocked|
|1234 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000 <br> 0000|Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> Likeness = 0 <br> System Locked Down|
