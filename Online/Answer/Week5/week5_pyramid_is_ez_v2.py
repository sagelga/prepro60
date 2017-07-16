""" Pyramid is EZ V.2 """
def main():
    """ main function """
    num = int(input())
    cnt1 = 0
    cnt2 = 0

    while cnt1 < num:
        cnt2 = 0
        cnt3 = 1
        while cnt2 < num - cnt1 - 1:
            print(" ", end='')
            cnt2 += 1
        while cnt3 <= cnt1:
            res = cnt3 % 10
            print(res, end='')
            cnt3 += 1
        while cnt3 > 0:
            res = cnt3 % 10
            print(res, end='')
            cnt3 -= 1
        cnt1 += 1
        print()

main()
