# Description
เมื่อพี่ๆได้พยายามจะเล่นเกมที่ให้บอกชื่อผลไม้ และสลับกับเพื่อนๆ ใครตอบช้า หรือตอบซ้ำ ก็ต้องออกจากเกมไป เป็น The Weakest Link กำจัดจุดอ่อน <br>
เรื่องตอบช้า อันนี้มันแล้วแต่ฝีมือคนตอบล้วนๆ แต่คำซ้ำนี่สิ อันนี้เช็คได้

พี่ๆอยากให้น้องเขียนโปรแกรมที่จะรับค่าและเช็คว่าตัวนั้นซ้ำหรือไม่ โดยการตอบว่า "Yes" สำหรับคำที่เคยพูดไปแล้ว (ซ้ำ) และ "No" สำหรับคำที่ยังไม่เคยพูดออกมา (ไม่ซ้ำ)

เอาเป็นว่า ไปดู Specs และ Sample Case จะดีกว่าเนอะ อิอิ

# Specification
|Input|Output|
|-|-|
|Input x+1 บรรทัด (String + Integer) <br> บรรทัดแรก บอกว่าจะมีคำศัพท์ที่ให้น้องเช็คกี่ตัว (เป็นค่า x) (Integer) <br> บรรทัดที่สองจนถึงค่า x+1 เป็นคำศัพท์ที่จะให้น้องเช็ค ว่าเคยมีอยู่แล้วหรือไม่ (String หรือ/และ Integer) <br>  <br> ในคำที่บอกว่าเคยมีแล้วหรือไม่ จะเช็คจาก input ก่อนหน้า ว่าเคย input มาแล้วหรือยัง <br>  <br> ตัวอักษรตัวใหญ่และตัวเล็ก จะถือว่ามีค่าเท่ากัน เช่น kuma = KUMA |Output x บรรทัด (String) <br> โดยหากว่าไม่ซ้ำ ให้ตอบว่า "No" <br> แต่หากว่าซ้ำ ให้ตอบว่า "Yes" |

# Sample Input / Output
|Sample Input|Sample Output|
|-|-|
|10 <br> My <br> Name <br> Is <br> Kumamon <br> at <br> Kumamoto <br> because <br> I <br> am <br> Kumamon|No <br> No <br> No <br> No <br> No <br> No <br> No <br> No <br> No <br> Yes|
|14 <br> Uppercase <br> and <br> LoWeRcAsE <br> does <br> not <br> matters <br> because <br> UPPERCASE <br> and <br> lowercase <br> is <br> the <br> same <br> text|No <br> No <br> No <br> No <br> No <br> No <br> No <br> Yes <br> Yes <br> Yes <br> No <br> No <br> No <br> No|
