""" Hot Cold """
def main():
    """ Main function """
    temp = int(input())
    if temp < 27:
        print("cold")
    elif temp <= 35:
        print("hot")
    elif temp <= 40:
        print("hot mak mak")
    else:
        print("die nae nae")

main()
