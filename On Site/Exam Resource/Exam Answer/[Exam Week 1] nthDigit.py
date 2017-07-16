"""
Sample Answer from P' Kumamon
This program will find the corresponding array
"""
def main():
    """Sample Answer from P' Kumamon"""
    response = int(input())
    number_sequence = '12345678910111213141516171819202122232425262728293031323334353637383940'
    if 0 < response < 52:
        print(number_sequence[response - 1])
    else:
        print("Out of Range")

main()
