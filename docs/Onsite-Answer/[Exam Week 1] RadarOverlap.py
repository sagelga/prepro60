"""
Sample Answer from P' Kumamon
This program will calculate that the beacon radius are merged or not
"""
def main():
    """Sample Answer from P' Kumamon"""
    beacon_x1 = float(input())
    beacon_y1 = float(input())
    radius1 = float(input())

    beacon_x2 = float(input())
    beacon_y2 = float(input())
    radius2 = float(input())

    length = (((beacon_x1 - beacon_x2)**2) + ((beacon_y1 - beacon_y2)**2)) ** 0.5

    if (radius1 + radius2) >= length:
        print('Yes')
    else:
        print('No')

main()
