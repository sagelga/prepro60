""" Arrow V1 """
def main():
    """ Main Function """
    num = int(input())

    for cnt in range(num):
        for _ in range(num - cnt):
            print(" ", end='')
        for cnt2 in range(2 * cnt + 1):
            if cnt2 == 0 or cnt2 == 2 * cnt or cnt2 == cnt:
                print("*", end='')
            else:
                print(" ", end='')
        print()
    for _ in range(num):
        print(" ", end='')
    print("*")
    for _ in range(num):
        print(" ", end='')
    print("*")

main()
