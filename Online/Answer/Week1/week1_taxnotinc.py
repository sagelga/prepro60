""" [Hardcore] [Week1] - Tax not included """
import math
def main():
    """ [Hardcore] [Week1] - Tax not included """
    subtotal = float(input())
    tax = float(input())
    print("Subtotal:", int(subtotal))
    str_tax = "Tax (" + str(tax * 100) + "%): " + str(int(tax * subtotal))
    print(str_tax)
    total = str(math.ceil(subtotal * (1 + tax)))
    print("Total: " + total)

main()
