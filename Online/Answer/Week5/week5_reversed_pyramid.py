""" Reversed Pyramid """
def main():
    """ Main Function """
    num = int(input())

    for cnt in range(num):
        for _ in range(cnt):
            print(" ", end='')
        for _ in range(2 * (num - cnt) - 1):
            print("*", end='')
        print()

main()
