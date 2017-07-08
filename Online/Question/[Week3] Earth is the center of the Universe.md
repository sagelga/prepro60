# Description
IT IS REAL

สำหรับโจทย์มงมงสัปดาห์นี้ ก็คงขาดไม่ได้กับการให้คำศัพท์อยู่กื่งกลางหล่ะจ้า

# Specification
| Input Specification | Output Specification |
| - | - |
| Input เป็น String ไม่เกินขนาด 40 ตัวอักษร <br> หากเกิน ก็ทำให้มันไม่เกินโดยการตัดออกไป  | Output 2 บรรทัด <br> บรรทัดแรก ให้ string ที่รับมาอยู่ตรงกลาง โดยให้มี \| ปิดซ้ายขวา โดยกรอบนั้นจะต้องมีขนาด 40 หรือ 41 ตัวอักษร <br> บรรทัดที่สอง ให้เขียนตาม Sample Testcase เลย แต่ space คือการชิดซ้าย-ขวาของน้องคือเท่าไหร่ แล้ว text length คือความยาวของตัวอักษร <br> <br>เอาเป็นว่า ดู Sample Testcase ดีกว่าครับ |


# Sample Case
Input :
```
Kumamoto
```
Output : 
```
|                Kumamoto                |
FOR DEBUG: Space = 16   Text Length = 8
```

Input :
```
123456789012345678901234567890
```
Output : 
```
|     123456789012345678901234567890     |
FOR DEBUG: Space = 5   Text Length = 30
```

Input :
```
1234567890123456789012345678901234567890
```
Output : 
```
|1234567890123456789012345678901234567890|
FOR DEBUG: Space = 0   Text Length = 40
```

Input :
```
Earth is flat
```
Output : 
```
|             Earth is flat             |
FOR DEBUG: Space = 13   Text Length = 13
```

Input :
```
12345678901234567890123456789012345678901234567890
```
Output : 
```
|1234567890123456789012345678901234567890|
FOR DEBUG: Space = -5   Text Length = 50
```
