""" The very best """
def main():
    """ Main Function """

    name1, value1 = calc()
    name2, value2 = calc()
    name3, value3 = calc()
    name4, value4 = calc()
    name5, value5 = calc()

    best = min(value1, value2, value3, value4, value5)

    print(name1 * (best == value1) + name2 * (best == value2) +
          name3 * (best == value3) + name4 * (best == value4) +
          name5 * (best == value5))

def calc():
    """ Value Calculate Function """
    name = input()
    price = float(input())
    weight = float(input())
    name2 = input()
    price2 = float(input())
    weight2 = float(input())
    value1 = price / weight
    value2 = price2 / weight2
    best = min(value1, value2)
    r_name = (name * (best == value1)) + (name2 * (best == value2))
    return r_name, best


main()
