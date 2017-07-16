""" Earth is the center 1 """
def main():
    """ Main function """
    text = input()
    space = (40 - len(text))//2
    print("|", " " * space, "%.40s" %text, " " * space, "|", sep='')
    print("FOR DEBUG: Space = ", space, "   Text Length = ", len(text), sep='')
main()
