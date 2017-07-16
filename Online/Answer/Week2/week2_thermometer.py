""" Temperature calculator """
def main():
    """ Main function """
    result = calculate(float(input()))
    print(result)

def calculate(farenheit):
    """ Take Farenheit and convert to Celsius """
    return round((farenheit - 32) / 9 * 5, 2)

main()
