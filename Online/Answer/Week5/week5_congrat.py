""" Congratulations I know you want in in in in in in in in in in in in in in in in in in in in """
def main():
    """ Main Function """
    string = input()

    for cnt in range(1, 101):
        print(string, " #", str(cnt), "\t\t", end='', sep='')
        if cnt % 5 == 0:
            print()

main()
