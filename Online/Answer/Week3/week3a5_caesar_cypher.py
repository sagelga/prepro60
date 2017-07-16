""" Week 3 & 5 Caesar Cypher """
def main():
    """ Main Function """
    string = input()

    for cha in string:
        print(chr(ord(cha)+3), end='')

main()
