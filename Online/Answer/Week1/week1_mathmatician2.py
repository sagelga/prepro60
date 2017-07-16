""" [Week 1] Mathmatician 2 """
import math
def main():
    """ main function """
    number = float(input())

    print(int(2 * math.pi * number), "cm")
    print(int(math.pi * number**2), "cm^2")
    print(int(4/3 * math.pi * number**3), "cm^3")

main()
