""" Decimal Converter """
# def main():
#     """ Main function """
#     number = int(input())

#     for cnt in range(2, 37):
#         print("Base ", cnt, ": ", convert(number, cnt), sep='')

# def convert(num, base):
#     """ Convert Function """
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if num < base:
#         return digits[num]
#     else:
#         return convert(num//base, base) + digits[num % base]

# main()

def main():
    """ Main Function """
    number = int(input())
    for index in range(2, 37):
        temp = number
        string = ""
        while temp >= index:
            string += convert(temp, index)
            temp = int(temp / index)
        if temp > 0:
            string += convert(temp, index)
        print("Base ", index, ": ", string[::-1], sep='')

def convert(temp, index):
    """ Convert Function """
    if temp % index <= 9:
        return str(temp % index)
    else:
        return str(chr(ord('A') + (temp % index - 10)))

main()
