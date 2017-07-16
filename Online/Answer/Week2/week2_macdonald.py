""" MacDonald """
def calc():
    """ Calculate Function """
    people = int(input())
    minute = int(input())
    second = int(input())

    second = min(second, 1)

    minute -= 120
    minute += second
    minute = max(minute, 0)


    print((320 * people) + (20 * people * minute))

calc()
calc()
calc()
calc()
calc()
