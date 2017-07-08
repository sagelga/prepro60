# Description
เปลี่ยนอารมณ์กันบ้าง

ให้น้องๆเขียนDocstringของโปรแกรมนี้ เอาแบบให้คนที่ไม่รู้เรื่องเกี่ยวกับโปรแกรมนี้เลย สามารถอ่านแล้วเข้าใจหลักการทำงานพอสังเขปได้
```python
"""DOCSTRING"""
def main(arg_1, arg_2, arg_3, arg_4, arg_5):
    """DOCSTRING"""
    minimum = min(arg_1, arg_2, arg_3, arg_4, arg_5)
    maximum = max(arg_1, arg_2, arg_3, arg_4, arg_5)
    average = avg(arg_1, arg_2, arg_3, arg_4, arg_5)
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Average:", average)

def avg(num_1, num_2, num_3, num_4, num_5):
    """DOCSTRING"""
    return (num_1+num_2+num_3+num_4+num_5)/5

main(int(input()), int(input()), int(input()), int(input()), int(input()))
```

# Specification
| Input Specification | Output Specification |
| - | - |


# Sample Case
| Sample Input | Sample Output |
| - | - |