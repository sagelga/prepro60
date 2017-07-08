# Description
<img src="https://cdn-starbucks.netdna-ssl.com/uploads/images/_framed/F7JHOenh-3500-2333.JPG" width="500px">

พี่คุมะมง และ เจ้าโซบะ ได้ไปที่ร้านกาแฟแห่งหนึ่ง ที่เพื่อนๆก็รู้ว่ามันแพง พี่มงก็ไปกิน

วันหนึ่ง พี่เกิดสงสัย ว่าหากว่าพี่อยากจะซื้อกาแฟซักแก้วนึง มันจะราคาซักเท่าไหร่กัน ไม่น่าจะแพงหรอกเนอะ (เหอๆ)

วันนี้ น้องมาช่วยพี่มงในการคำนวณราคากาแฟของร้านนี้กันครับ

## Menu
เป็นราคาของแก้วขนาด Tall

ทางร้านจะมีเครื่องดึ่มปั่นเพียงบางรายการเท่านั้น (หากมี - หมายความว่าทางร้านไม่ขาย)

| เครื่องดึ่ม    |ราคาสำหรับเครื่องดึ่มเย็นและร้อน (Hot or Iced)|ราคาสำหรับเครื่องดึ่มปั่น (Frappe)|
| :------------- | :------------- | :------------- |
| Black Coffee| 90|-|
|Americano|105|-|
|Espresso|85|140|
|Latte|115|125|
|Mocha|130|140|
|Cappuccino|115|-|
|Caramel Macchiato|140|-|
|Green Tea Latte|135|165|
|Chocolate Latte|110|140|

## Toppings
โดยการใช้ + แทน 1 หน่วย topping หากไม่มีจะไม่เขียน

|Extra Shot|Extra Caramel|+ JavaChip|
|-|-|-|
|+15|+10|+30|

## Choose your cup size
กาแฟร้อนจะมีให้เลือกตั้งแต่ Short จนถึง Venti <br>
หากเป็นเครื่องดึ่มปั่น และ เย็น จะมีให้เลือกตั้งแต่ Tall จนถึง Venti เท่านั้น

|Short (Hot only)|Tall|Grande|Venti|
|-|-|-|-|
|-15 baht|+0 baht|+15 baht|+30 baht|

ทางร้านไม่จำกัดปริมาณท้อปปี้งและเมนูที่จะใส่ท้อปปี้ง

# Specification
|Input|Output|
|-|-|
|1 บรรทัด <br> เป็นตาม format โดยเรียงจาก <br> ขนาดกาแฟ, <br> ประเภทเครื่องดึ่ม, <br> เมนูเครื่องดื่ม, <br> ท้อปปี้ง|1 บรรทัด <br> เป็นราคาของแก้วนี้ <br> แต่หากข้อมูลให้มาไม่ครบถ้วน หรือไม่มีในเมนู​ <br><br> หากขนาดผิด หรือ ขนาดขัดแย้งกับร้อน/เย็น/ปั่น ให้เขียนว่า 'Invalid size' <br> หากเมนูผิด หรือ เมนูนี้ไม่มีประเภทปั่น ให้เขียนว่า 'Invalid type' <br> หากประเภทเครื่องดื่มผิด (ร้อน/เย็น/ปั่น) ให้เขียนว่า 'Invalid beverage' <br> หากท้อปปี้งผิด ให้เขียนว่า 'Invalid topping' <br>|

# Sample Input / Output
|Input|Output|
|-|-|
|Grande Iced Green Tea|150 baht|
|Grande Hot Green Tea +Shot|180 baht|
|Grande Iced Green Tea ++Shot|210 baht|
|Grande Iced Green Tea +Shot +Caramel|205 baht|
|Venti Mocha +JavaChip|185 baht|
|Small Iced Espresso +JavaChip|Invalid size|
|Short Iced Espresso +Shot|Invalid size|
|Venti Chadum Yen Coffee|Invalid type|
|Venti Frappe Black Coffee|Invalid type|
|Short Iced Espresso +Milk|Invalid topping|
|Bag Cold Oleang ++Sugar|Invalid size <br> Invalid type <br> Invalid beverage <br> Invalid topping|
