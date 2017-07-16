""" 2 input """
def main():
    """ Main function """
    inp1 = input()
    if inp1.isalpha():
        inp2 = input()
        print(inp1, inp2)
    else:
        print(inp1)

main()
