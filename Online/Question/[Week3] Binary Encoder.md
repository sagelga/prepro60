# Description
Encode คือการแปลงให้อีกอย่างนึง เป็นอีกอย่างนึง

วันนี้ พี่มงจะมาสอนวิธีการเปลี่ยน Decimal (เลขฐาน 10) เป็น Binary (เลขฐาน 2)

จ่ะ ดังนั้น แปลงเลข Decimal to Binary ให้หน่อยจิ

# Specification
| Input Specification | Output Specification |
| - | - |
| Input 1 บรรทัด เป็น integer เต็มบวก | Output 1 บรรทัด เป็นเลข Binary จำนวน 8 bit เท่านั้น <br> ถ้าเกินก็ตัดข้างหน้าออก ถ้าขาดก็เติม 0 ให้เต็ม 8 bit |


# Sample Case
| Sample Input | Sample Output |
| - | - |
| 255 | 11111111 |
| 0 | 00000000 |
| 25 | 00011001 |
| 32 | 00100000 |
| 99999 | 10011111 |