""" upper lower """
def main():
    """ Main function """
    string = input()
    if len(string) == 1 and string.islower():
        print(string.upper())
    elif len(string) == 1 and string.isupper():
        print(string.lower())
    else:
        print("eating -", string)
main()
