""" Congratulations """
def main():
    """ Main Function """
    string = input()
    display(string, 1)
    display(string, 6)
    display(string, 11)
    display(string, 16)
    display(string, 21)
    display(string, 26)
    display(string, 31)
    display(string, 36)
    display(string, 41)
    display(string, 46)
    display(string, 51)
    display(string, 56)
    display(string, 61)
    display(string, 66)
    display(string, 71)
    display(string, 76)
    display(string, 81)
    display(string, 86)
    display(string, 91)
    display(string, 96)

def display(string, num):
    """ Display Function """
    print(string + " #" + str(num) + "\t\t", end="")
    print(string + " #" + str(num+1) + "\t\t", end="")
    print(string + " #" + str(num+2) + "\t\t", end="")
    print(string + " #" + str(num+3) + "\t\t", end="")
    print(string + " #" + str(num+4), end="\n")

main()
