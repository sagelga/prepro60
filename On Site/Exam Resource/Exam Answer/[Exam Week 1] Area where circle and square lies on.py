"""
Sample Answer from P' Kumamon
This program will calculate area where circle and square lies on
"""
def main():
    """Sample Question from P' Kumamon"""
    length = int(input())
    area_circle = (22/7) * (length/2)**2
    area_square = length**2
    area = (area_square - area_circle) / 4
    print("%.2f" %area)
main()
