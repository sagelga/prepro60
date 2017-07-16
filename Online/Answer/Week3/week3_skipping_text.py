""" Skipping Text """
def main():
    """ Main function """
    text = input()
    print("%.10s" %text)
    print("%30.10s" %text)
    print("%-30.10s" %text)
    print(text[2::])
    print(text[5::])
    print(text[2:5])
    print(text[::2])
    print(text[::5])
    print(text[2::2])
    print(text[0])

main()
