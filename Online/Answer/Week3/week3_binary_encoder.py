""" Binary Encoder """
def main():
    """ Main function """
    num = bin(int(input()))[2:]
    num = num[:-9:-1]
    num = num[::-1]
    print("%0.8d" %int(num))

main()
