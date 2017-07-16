""" Numerical """
def main():
    """ Main function """
    print(find(input(), 1) +
          find(input(), 2) +
          find(input(), 3) +
          find(input(), 4) +
          find(input(), 5))

def find(number, digit):
    """ Find function """
    return int(number[5 - digit])

main()
