"""
Sample Answer from P' Kumamon
This program will calculate the ticket price for all customer count
"""
def main():
    """Sample Answer from P' Kumamon"""
    day = input()
    count = int(input())

    if day == "monday" or day == "tuesday":
        price = 120
    elif day == "wednesday":
        price = 80
    else:
        price = 140
    print(count * price)

main()
