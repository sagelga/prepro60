# Description
One morning later.....

เขียนอะไรมานั่น ไม่รู้เรื่องโหวยยยยย

พี่ว่า หน้าจอของเค้ามันจะเล็กไปหน่อย กดถูกๆผิดๆบ้าง

วันนี้ น้องจึงเปิดโจทย์ข้อนี้ขื้นมา เพื่อมาช่วยพี่มง autocorrect string ที่มีค่าเท่ากับตัวเลข (ONE = 1, TWO = 2) ให้หน่อยสิ

ตามสไตล์โจทย์มงมงแล้ว.......เชิญอ่าน Specs และ Sample Case เลยครับ

# Specification
| Input Specification | Output Specification |
| - | - |
| Input 1 บรรทัด เป็นคำที่มีความหมายเป็นตัวเลข <br> (Input ที่เป็นไปได้ มีเพียง ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE เท่านั้น) <br> โดยคำพวกนั้น จะถูกเรียงอย่างเละเทะ อ่านไม่ออก และสลับ Uppercase + Lowercase เละเทะ | Output เป็นตัวเลข ที่มีความหมายเหมือนกับ input ที่ถูกเรียงใหม่แล้ว <br> (Output ที่เป็นไปได้ มีเพียง 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 เท่านั้น) |


# Sample Case
| Sample Input | Sample Output |
| - | - |
| OTW | 2 |
| SeveN | 7 |
| ENO | 1 |