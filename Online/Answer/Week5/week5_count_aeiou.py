""" Count AEIOU """
def main():
    """ Main Function """
    string = input()
    cnt = 0

    for cha in string:
        if cha in "aeiouAEIOU":
            cnt += 1

    print(cnt)


main()
