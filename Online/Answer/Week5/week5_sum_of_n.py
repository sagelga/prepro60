""" Sum of N """
def main():
    """ Main Function """
    siz = int(input())
    res = 0

    for _ in range(siz):
        res += int(input())

    print(res)

main()
