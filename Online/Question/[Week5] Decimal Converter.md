# Description
สวัสดีครับ พี่มงเอง

ช่วงปิดเทอมของพี่ พี่ก็ได้ไปย้อนดู lecture เก่าๆของพี่เอง อันนึงเป็นวิชาเลขครับ วิธีที่จะแปลงเลขฐานนั่นเอง

แต่การแปลงเลขฐานบน Python นั้นก็มีหลักๆอยู่แล้ว คือ Binary, Hexadecimal, Octadecimal, Decimal

แต่มันจะไปสนุกอะไร ถ้ามีให้ใช้แค่นี้

ดังนั้นเราจะทำให้มัน Hardcore ไปเลย คือเอาตั้งแต่ ฐาน 2 ถึง 35 เลย อิอิ

ดู Sample Testcase น้องๆคงจะดูออกเนอะ :)

0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

กรุณาทำโปรแกรมให้ไม่ runtime error นะครับ (เขียนโค้ดให้มันไม่คิดมาก เดี๋ยวตายเอา)

# Specification
| Input Specification | Output Specification |
| - | - |
| Input 1 บรรทัด เป็นเลขฐาน 10 | Output 34 บรรทัด แต่ละบรรทัดคือผลลัพท์การแปลงเลขฐาน <br> ตั้งแต่ ฐาน 2 ถึง 35 โดยมีการเขียนกำกับไว้ด้วย ว่าแปลงเป็นฐานอะไร |


# Sample Case
| Sample Input | Sample Output |
| - | - |
| 36 | Base 2: 100100 <br> Base 3: 1100 <br> Base 4: 210 <br> Base 5: 121 <br> Base 6: 100 <br> Base 7: 51 <br> Base 8: 44 <br> Base 9: 40 <br> Base 10: 36 <br> Base 11: 33 <br> Base 12: 30 <br> Base 13: 2A <br> Base 14: 28 <br> Base 15: 26 <br> Base 16: 24 <br> Base 17: 22 <br> Base 18: 20 <br> Base 19: 1H <br> Base 20: 1G <br> Base 21: 1F <br> Base 22: 1E <br> Base 23: 1D <br> Base 24: 1C <br> Base 25: 1B <br> Base 26: 1A <br> Base 27: 19 <br> Base 28: 18 <br> Base 29: 17 <br> Base 30: 16 <br> Base 31: 15 <br> Base 32: 14 <br> Base 33: 13 <br> Base 34: 12 <br> Base 35: 11 <br> Base 36: 10 |
| 5555 | Base 2: 1010110110011 <br> Base 3: 21121202 <br> Base 4: 1112303 <br> Base 5: 134210 <br> Base 6: 41415 <br> Base 7: 22124 <br> Base 8: 12663 <br> Base 9: 7552 <br> Base 10: 5555 <br> Base 11: 41A0 <br> Base 12: 326B <br> Base 13: 26B4 <br> Base 14: 204B <br> Base 15: 19A5 <br> Base 16: 15B3 <br> Base 17: 123D <br> Base 18: H2B <br> Base 19: F77 <br> Base 20: DHF <br> Base 21: CCB <br> Base 22: BAB <br> Base 23: ABC <br> Base 24: 9FB <br> Base 25: 8M5 <br> Base 26: 85H <br> Base 27: 7GK <br> Base 28: 72B <br> Base 29: 6HG <br> Base 30: 655 <br> Base 31: 5O6 <br> Base 32: 5DJ <br> Base 33: 53B <br> Base 34: 4RD <br> Base 35: 4IP <br> Base 36: 4AB |