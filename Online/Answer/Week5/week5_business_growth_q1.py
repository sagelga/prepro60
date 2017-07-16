""" Business Growth Q1"""
def main():
    """ Main Function """
    num = int(input())

    for cnt in range(1, num + 1):
        for cnt2 in range(1, cnt + 1):
            print("%.2d " %cnt2, end='')
        print()

main()
