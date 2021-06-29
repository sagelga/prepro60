"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    total = 0 # Accumulate all input that follow rules
    for i in range(1, 9999999):
        number = input()

        if not (number = int(number)):
            if i == 1:
                print("Python is very Ez")
                break
            printer(i, total)
            break
        else:
            total += int(number)

def printer(divident, total):
    """This is a sample answer from P' Kumamon"""
    print("Sum of number is %d"%total)
    print("Average is : %.2f"%total/divident)

main()
