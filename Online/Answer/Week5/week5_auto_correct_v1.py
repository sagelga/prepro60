""" Very Weak Transmission """
def main():
    """ Main Function """
    string = input().lower()
    word = []

    for ccc in string:
        word.append(ccc)
    word.sort()

    num = "".join(word)

    if num == "eorz":
        print(0)
    elif num == "eno":
        print(1)
    elif num == "otw":
        print(2)
    elif num == "eehrt":
        print(3)
    elif num == "foru":
        print(4)
    elif num == "efiv":
        print(5)
    elif num == "isx":
        print(6)
    elif num == "eensv":
        print(7)
    elif num == "eghit":
        print(8)
    elif num == "einn":
        print(9)

main()
