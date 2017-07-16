""" Card Maker Problem """
def main():
    """ Main Function """
    sender = input()
    receiver = input()
    line_1 = input()
    line_2 = input()

    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*  Hi %-43s*" %receiver)
    print("*  %-46s*" %line_1)
    print("*  %-46s*" %line_2)
    print("*" + " " * 48 + "*")
    print("*%48s*" %"Thanks,  ")
    print("*%46s  *" %sender)
    print("*" + " " * 48 + "*")
    print("*" * 50)


main()
