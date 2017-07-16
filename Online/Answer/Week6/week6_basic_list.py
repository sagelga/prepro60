""" Basic List """
def main():
    """ Function Main """
    vovel = 0
    text = input()
    length = len(text)
    for ccc in text:
        if ccc in 'aeiouAEIOU':
            vovel += 1
    print(length - vovel, end=' ')
    for _ in range(vovel):
        print("*", end='')

main()
