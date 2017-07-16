""" Base 2 Average """
def main():
    """ Main function """
    avg1 = avg(convert(), convert(), convert(), convert(), convert())
    avg2 = avg(convert(), convert(), convert(), convert(), convert())

    result = (avg1 + avg2) / 2

    print(result)

def convert():
    """ Convert base 2 to 10 """
    number = int(input(), 2)
    return number

def avg(num1, num2, num3, num4, num5):
    """ Average function """
    return (num1 + num2 + num3 + num4 + num5) / 5

main()
