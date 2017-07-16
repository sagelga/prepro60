""" a^n """
def calc(base, exp):
    """ Calculate Function """
    base2 = base
    if base < 0:
        base = 0 - base
    if exp == 0:
        return 1
    ans = base
    inc = base

    for _ in range(1, exp):
        for _ in range(1, base):
            ans += inc
        inc = ans

    if base2 < 0 and exp % 2 == 1:
        ans = 0 - ans

    return ans

def main():
    """ Main Function """
    base = int(input())
    exp = int(input())

    print(calc(base, exp))

main()
