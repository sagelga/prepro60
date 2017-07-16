""" Basic List 4 """
def main():
    """ Function Main """
    text = list()
    for _ in range(5):
        text += [input()]
    text[0], text[4] = text[4], text[0]
    print(text)

main()
