""" Expensive Vovel """
def main():
    """ Main function """
    string = input()

    string = string.replace("a", "-")
    string = string.replace("A", "-")
    string = string.replace("e", "-")
    string = string.replace("E", "-")
    string = string.replace("i", "-")
    string = string.replace("I", "-")
    string = string.replace("o", "-")
    string = string.replace("O", "-")
    string = string.replace("u", "-")
    string = string.replace("U", "-")

    print(string)

main()
