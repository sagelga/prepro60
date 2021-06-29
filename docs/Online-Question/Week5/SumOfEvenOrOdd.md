# Description
จงสร้างโปรแกรมบวกค่าเลขคู่หรือเลขคี่

โดยโปรแกรมจะบอกน้องว่าให้บวกเลข ที่เป็นเลขคู่ หรือ เลขคี่ และให้น้องรับค่าไปเรื่อยๆจนตัวเลขที่ได้รับค่ามาคือ 0

# Specification
| Input Specification | Output Specification |
| - | - |
| บรรทัดแรก รับ string 1 บรรทัด <br> ตั้งแต่บรรทัดที่ 2 เป็นต้นไป รับค่าไปเรื่อยๆ และหยุดเมื่อได้รับค่าเป็น 0 | บรรทัดเดียว เป็น ผลบวกทั้งหมด แต่ถ้าหากไม่ใช่ทั้งคู่ให้แสดงว่า "Error, stringที่รับเข้ามา is not even and odd." |


# Sample Case
| Sample Input | Sample Output |
| - | - |
| odd <br> 1 <br> 2 <br> 0 | 1 |
| even <br> 1 <br> 2 <br> 0 | 2 |
| odd <br> 1 <br> 2 <br> 3 <br> 4 <br> 5 <br> 0 | 9 |
| ABCDE | Error, ABCDE is not even and odd. |