""" [Week 1] Distance """
import math
def main():
    """ main function """
    px1 = float(input())
    py1 = float(input())
    px2 = float(input())
    py2 = float(input())

    print("Distance =", int(math.hypot(px2 - px1, py2 - py1)))

main()
