"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    number = int(input())
    while number > 1:
        if number % 2 == 1:
            number += 1
        else:
            number /= 2
        print(number, sep=" ")

main()
