# Description
น้องได้รับจ้างเขียนโปรแกรมตรวจเช็คความปลอดภัยของ password ให้กับเว็บคณะ IT ชื่อดังย่านลาดกระบัง โดยมี Requirement ดังนี้
- รับ username และ password จำนวน n คน
- ให้หาว่า password ของ user นั้นๆ สามารถเอาไปใช้ได้หรือไม่ ถ้าใช้ได้ให้แสดงระดับความปลอดภัยของ password

โดย password จะใช้ได้ก็ต่อเมื่อ password มีความยาว 6 ตัวหรือมากกว่าและไม่มีสัญลักษณ์ใดๆทั้งนั้น

ถ้าใช้ไม่ได้ ให้แสดงว่า Invalid แต่ถ้าใช้งานได้ ให้ตรวจสอบดูว่ามีความปลอดภัยอยู่ในระดับไหน โดยมีเงื่อนไขคือ
- มีตัวอักษรภาษาอังกฤษตัวพิมพ์เล็ก
- มีตัวอักษรภาษาอังกฤษตัวพิมพ์ใหญ่
- มีตัวเลข

ซึ่งระดับความปลอดภัยจะแบ่งเป็นสามระดับ
- ผ่าน 1 เงื่อนไข = ความปลอดภัยต่ำ (Low)
- ผ่าน 2 เงื่อนไข = ความปลอดภัยปานกลาง (Medium)
- ผ่าน 3 เงื่อนไข = ความปลอดภัยสูง (High)

ส่วนในการแสดงผลเราจะแสดง
1. Username
2. Password เป็นตัว * มีความยาวเท่ากับขนาดของpassword
3. ระดับความปลอดภัย (Low, Medium, High) หรือ Invalid

[Example]
Username: it60070888 / Password: ******* (Security-Level: High)
Username: helloworld / Password: ******* (Invalid)

# Specification
|Input|Output|
|-|-|
|1+n บรรทัด <br> บรรทัดแรกเป็น Integer เจำนวน user <br> บรรทัดต่อมาเป็น string username password|n บรรทัด <br> ตามรูปแบบด้านบนหรือดูใน sample i/o ก็ได้ |

# Sample Input / Output
Input :
```
6
it59070777 VERYsecure123
admin 1234
root 1a2b3c
it60070789 helloworld
guest01 12xRzz
guest07 1416Z
```

Output :
```
Username: it59070777 / Password: ************* (Security-Level: High)
Username: admin / Password: **** (Invalid)
Username: root / Password: ****** (Security-Level: Medium)
Username: it60070789 / Password: ********** (Security-Level: Low)
Username: guest01 / Password: ****** (Security-Level: High)
Username: guest07 / Password: ***** (Invalid)
```

Input :
```
4
nongbanklnwza007 PASSWORDyakmakmak123
guestaccount1 HZXypp45
guestaccount2 @itkmitl01
guestaccount3 Lx019
```

Output :
```
Username: nongbanklnwza007 / Password: ******************** (Security-Level: High)
Username: guestaccount1 / Password: ******** (Security-Level: High)
Username: guestaccount2 / Password: ********** (Invalid)
Username: guestaccount3 / Password: ***** (Invalid)
```
