""" Pascal Triangle """
import math

def ncr(nnn, rrr):
    """ nCr Function """
    result = math.factorial(nnn) / (math.factorial(nnn - rrr)  * math.factorial(rrr))
    return int(result)

def main():
    """ Main Function """
    num = int(input())
    for cnt1 in range(num):
        for cnt2 in range(cnt1 + 1):
            print(ncr(cnt1, cnt2), end=' ')

main()
