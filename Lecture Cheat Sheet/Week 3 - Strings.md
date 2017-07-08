# Python Week 3 by P’ Kumamon (Strings)

Copyright by P' Kumamon IT14.
For education purpose only

## Follow me on GitHub
![https://github.com/sagelga](/Reference%20Photos/GitHub-Profile-Mobile.png)

----------
# String คืออะไร
String เป็นตัวแปรประเภทนึง ที่เก็บ character ไว้หลายๆตัว อาจจะเพียง 2 ตัวก็ได้ หรือจะเป็น ล้านๆตัวก็ได้

Python นั้น จะเก็บข้อมูล String ไว้ในแบบ Array หรือว่ากล่อง(ถ้าจะให้เข้าใจง่ายๆ) โดยกล่องๆนึง มี character อยู่หนึ่งตัว

และ โกดังคือตัวแปร String ที่มีหน้าที่เก็บกล่อง(character) โดยไม่สนใจว่าโกดังจะเล็กไปหรือใหญ่ไปหรือไม่ (Compiler จะทำหน้าที่คำนวณเอง ไม่เหมือนภาษาคอมพิวเตอร์อื่น)

### วิธีให้ตัวแปรเก็บค่า String
```python
blank_space = "" # ถ้าเป็นภาษาคอมพิวเตอร์อื่นๆ ต้องประกาศตัวแปรก่อน Python ไม่ต้อง
text = "Hello World"
mood = "Not that much 555"
number = "12" # ค่า '12' (string) จะไม่เท่ากับ 12 (integer) นะครับ ต้องระวังให้ดี
```

### ถ้าต้องการเรียกตัวอักษรบางตัวมาใช้เท่านั้น
```python
How to use:
<variable>[start:stop:step]

# Start -> ให้เรื่มตั้งแต่ตัวอักษรไหน       (Default: 0)
# Stop  -> ให้หยุดที่ตัวอักษรไหน         ( Required )
# Step  -> ข้ามตัวอักษรเมื่อครบทุกๆ x ตัว  (Default: 1)
```

### ปรี้นท์ตัวอักษรออกมาตัวเดียว
```python
var = "ABCD"
print(var[0]) # Prints out "A" (A is in the 0th number array)
```

ถ้ายังไม่เข้าใจ ดูตารางเปรียบเทียบเอาครับ

| **String (ชื่อ var)**   | A | B | C | D |
| ------------------ | - | - | - | - |
| **ตำแหน่งของ Array บน string**   | 0 | 1 | 2 | 3 |
| **ตำแหน่งตัวอักษรจริง** | 1 | 2 | 3 | 4 |

ระวังว่าตำแหน่งของ array จะเรื่มจาก 0 เสมอ ไม่เหมือนคนนะครับ ที่เรื่มนับจาก 1 เลย

### หาก Stop เป็นตัวเลขติดลบ
```python
var = "ABCD"
print(var[-1]) # Prints out "D" (D is the first one from the last)
```

### Array จริงน้อยกว่าที่เราต้องการเรียก
```python
var = "ABCD"
print(var[50]) # เกิด error เพราะว่า array ตัวที่ 50 ไม่มีจริง
```

### การ Print ตัวอักษรหลายตัว (แต่ไม่ใช่ทุกตัว)
```python
var = "ABCD"
print(var[0:2]) # Prints out "AB" (โดยเรื่มเอาจากตัวที่ 0 จนถึงตัวที่ 1 (ระวังนะครับ ข้อนี้ผิดกันเยอะมากเลย))
```

### เรื่มต้นและต่อเนื่องไป
```python
var = "My name is Kumamon, and I love eating"
print(var[4:]) # Prints out "name is Kumamon, and I love eating" (Starting from 4th array number)
```

### Start from beginning to stop
```python
var = "My name is Kumamon, and I love eating"
print(var[:7])
# Prints out "My name" (Starting from 0th array number to the 7th)
```

### Skips every
```python
var = "ABABABAB"
print(var[::2])
# Prints out AAAA (Skips after logical number hits every 2, which is B)
```

### Inverse Skips every
```python
var = "ABABABAB"
print(var[::-2])
# Prints out BBBB (Skips after logical number hits every -2, which is A)
```

----------
# Modifying Strings

NOTE: Please go take a look at Week 1. There is a few that you already know
+Python Week 1 by P’ Kumamon (I/O)

Variable Types and how to print like C

| **Use**      | %s     | %d      | %f    | %e                     |
| ------------ | ------ | ------- | ----- | ---------------------- |
| **To print** | String | Integer | Float | Scientific Significant |


### Doing it like C

    var = "My name is Kumamon"
    print(">> %s <<" %var)
    # Prints out ">> My name is Kumamon <<"

## String Type Manipulation

| Type      | %10s     | %-10s    | %.10s      | %-.10s     | %10.10s | %-10.-10s |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      |

```python
text = "ABC"

print("%4s" %text) # Prints out " ABC"

print("%-4s" %text) # Prints out "ABC "

print("%.2s" %text) # Prints out "AB"

print("%-.2s" %text) # Prints out "AB"

print("%5.2s" %text) # Prints out "   AB"

print("%-5.2s" %text) # Prints out "AB   "
```

## Integer Type Manipulation

| Type      | %10d     | %-10d    | %.10d      | %-.10d     | %10.10d | %-10.-10d | %0.10d                          |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- | ------------------------------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      | Aligning                        |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      | Right
(Add 0 instead of space) |

```python
number = 12345

print("%10d" %number)
# Prints out "     12345"

print("%-10d" %number)
# Prints out "12345     "

print("%.3d" %number)
# Prints out "12345"

print("%-.3d" %number)
# Prints out "12345"

print("%0.10d" %number)
# Prints out 0000012345
```

## Float Type Manipulation

| Type      | %10f     | %-10f    | %.10f      | %-.10f     | %10.10f | %-10.-10f |
| --------- | -------- | -------- | ---------- | ---------- | ------- | --------- |
| For       | Aligning | Aligning | Cut String | Cut String | Both    | Both      |
| Alignment | Right    | Left     | Right      | Left       | Right   | Left      |

```python
print("%10f" %number)
# Prints out "123.456700"

print("%-10f" %number)
# Prints out "123.456700"

print("%.2f" %number)
# Prints out "123.46"

print("%-.2f" %number)
# Prints out "123.46"

print("%10.3f" %number)
# Prints out "   123.457"

print("%-10.3f" %number)
# Prints out "123.457   "
```

## Scientific Significant Type Manipulation

```python
print("%e" %number)
# Prints out '1.234567e+02'
```
----------

# Strings to ASCII
![https://i.stack.imgur.com/X4yts.png](https://i.stack.imgur.com/X4yts.png)


# String to ASCII (Decimal)
```python
print(ord('A')) # Print out 65
```

# ASCII (Decimal) to String
```python
print(chr(65)) # Print out 'A'
```

# Alters String ASCII
```python
print(chr(65+1)) # Print out 'B'
```

# Referencing number from variable
```python
var = 75
print(chr(var)) # Print out 'K'
```

# Alters String ASCII from character
```python
print(chr(ord('A')+1)) # Print out 'B'
```

# String to change case
```plain
Convert character/text to lowercase -> .lower()
Convert character/text to uppercase -> .upper()
Convert character/text from lower to upper vice versa -> .swapcase()

Check character/text is lowercase -> .islower()
Check character/text is uppercase -> .isupper()
Check character/text is a number -> .isdigit()
Check character/text is an alphabet -> .isalpha()
```

### Using .lower()
```python
text = "KUMAMON"
text = "KuMaMoN"
text = "kumamon"
print(text.lower()) # All will print out "kumamon"
```

### Using .upper()
```python
text = "KUMAMON"
text = "KuMaMoN"
text = "kumamon"
print(text.upper()) # All will print out "KUMAMON"
```

### Using .swapcase()
```python
text = "Kumamon"
print(text.swapcase()) # Prints out "kUMAMON"

text = "KuMaMoN"
print(text.swapcase()) # Prints out "kUmAmOn"
```

### Using .isupper() & .islower()
```python
How to use:
<input variable>.islower()
-> Returns True or False

<input variable>.isupper()
-> Returns True or False

text = "K"
return text.islower() # Returns false
return text.isupper() # Returns true

text = "k"
return text.islower() # Returns true
return text.isupper() # Returns false
```

### Using .isdigit() & .isalpha()
```python
How to use:
<input variable>.isdigit()
-> Returns True or False

<input variable>.isalpha()
-> Returns True or False

text = "12"
return text.isdigit() # Returns true
return text.isalpha() # Returns false

text = "ABC"
return text.isdigit() # Returns false
return text.isalpha() # Returns true
```

----------
# String with array counts and find
```plain
Finding character in text -> .find()
Count character in text that satisfies search query -> .count()
Finding text in array -> .index()

Count all character in text -> len()
```

### Using .find()
```python
How to use:
<variable name>.find("<character/text you want to find>")
-> Return as the lowest array number

# 1 occurence character
var = "ABCDE"
return var.find("A") # Returns 0

# 2 occurence character
var = "ABCDEAAAAA"
return var.find("A") # Returns 0

# Non occurence character
var = "ABCDE"
return var.find("F") # Returns -1

# Using more than 1 character
var = "Kumamon is happy"
return var.find("Kuma") # Returns 0

# Using more than 1 character + 2 occurence
var = "Kumamon is happy, Kumamon is happy"
return var.find("Kuma") # Returns 0
```

### Using .count()
```python
How to use:
<variable name>.count("<character/text you want to count>")
-> Returns the amount of character count.

# 1 occurence character
var = "ABCDE"
return var.count("A") # Returns 1

# 2 occurence character
var = "ABCDEAAAAA"
return var.count("A") # Returns 6

# Non occurence character
var = "ABCDE"
return var.count("F") # Returns 0

# Using more than 1 character
var = "Kumamon is happy"
return var.count("Kuma") # Returns 1

# Using more than 1 character + 2 occurence
var = "Kumamon is happy, Kumamon is happy"
return var.count("Kuma") # Returns 2
```

### Using len()
```python
How to use:
len(<variable you want to count character>)
Returns number of elements/character in array/text

# Using to count strings
return len("Kumamon") # Returns 7

# Using to count strings in variable
var = "Kumamon"
return len(var) # Returns 7

# Using to count elements in array
var = [11,12,13,14,15]
return len(var) # Retuns 5
```
---
# Strings to other base numeric number

### Using bin()
```python
How to use:
bin(<decimal integer>) # Built-in function. Returns the binary number (Base 2)

Example:
print(bin(12345)) # Prints out 0b11000000111001
```

### Using hex()
```python
How to use:
hex(<decimal integer>) # Built-in function. Returns the hexadecimal number (Base 6)

Example:
print(hex(12345)) # Prints out 0x3039
```

### Using oct()
```python
How to use:
oct(<decimal integer>) # Built-in function. Returns the octal number (Base 8)

Example:
print(oct(12345)) # Prints out 0o30071
```
