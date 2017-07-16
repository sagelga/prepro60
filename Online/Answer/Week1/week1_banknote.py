""" Bank Notes """
def main():
    """ Main Function """
    money = int(input())

    thousand = money // 1000
    money -= (thousand * 1000)
    fivehundred = money // 500
    money -= (fivehundred * 500)
    hundred = money // 100
    money -= (hundred * 100)
    fty = money // 50
    money -= (fty * 50)
    twenty = money // 20

    print(thousand)
    print(fivehundred)
    print(hundred)
    print(fty)
    print(twenty)

main()
