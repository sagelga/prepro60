# Description
โปรแกรมจะให้ text ความยาวไม่รู้เท่าไหร่ แต่ต้องออกตาม Sample Output ครับ

ไปดูดีกว่าเนอะ

บอกเลยว่าง่ายม๊ากกก

3 ตัวแรกใช้ %

7 ตัวหลังใช้ [::]

# Specification
| Input Specification | Output Specification |
| - | - |
| Input เป็น text ที่มีความยาวแตกต่างกัน | Output ก็ดูเอาเนอะ ว่าออกอะไรไปบ้าง มีทั้งหมด 10 บรรทัดครับ <br> 3 ตัวแรกใช้ % <br> 7 ตัวหลังใช้ [::] |


# Sample Case
Input :
```
I love Kumamon. I will not have a good dream without you.
```
Output : 
```
I love Kum
                    I love Kum
I love Kum                    
love Kumamon. I will not have a good dream without you.
e Kumamon. I will not have a good dream without you.
lov
Ilv uao.Iwl o aeago ra ihu o.
Iea lteorwuu
lv uao.Iwl o aeago ra ihu o.
I
```

Input :
```
1010 2020 3030 4040 5050 6060
```
Output : 
```
1010 2020 
                    1010 2020 
1010 2020                     
10 2020 3030 4040 5050 6060
2020 3030 4040 5050 6060
10 
11 0033 0055 00
123456
1 0033 0055 00
1
```

Input :
```
ABCDE
```
Output : 
```
ABCDE
                         ABCDE
ABCDE                         
CDE

CDE
ACE
A
CE
A
```

Input :
```
ABCDEF
```
Output : 
```
ABCDEF
                        ABCDEF
ABCDEF                        
CDEF
F
CDE
ACE
AF
CE
A
```

Input :
```
ABCDEFGHIJ
```
Output : 
```
ABCDEFGHIJ
                    ABCDEFGHIJ
ABCDEFGHIJ                    
CDEFGHIJ
FGHIJ
CDE
ACEGI
AF
CEGI
A
```

Input :
```
ABCDEFGHIJKL
```
Output : 
```
ABCDEFGHIJ
                    ABCDEFGHIJ
ABCDEFGHIJ                    
CDEFGHIJKL
FGHIJKL
CDE
ACEGIK
AFK
CEGIK
A
```
