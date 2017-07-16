""" Triangle """
def main():
    """ Main function """
    num = int(input())

    for cnt in range(num):
        for _ in range(num - cnt - 1):
            print(" ", end='')
        for _ in range(cnt + 1):
            print("*", end='')
        print()

main()
