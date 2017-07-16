""" Print m to n """
def main():
    """ Main function """
    start = int(input())
    stop = int(input())
    if start - stop < 0:
        for cnt in range(start, stop + 1):
            print(cnt, " ", sep='', end='')
    elif start - stop > 0:
        for cnt in range(start, stop - 1, -1):
            print(cnt, " ", sep='', end='')

main()
