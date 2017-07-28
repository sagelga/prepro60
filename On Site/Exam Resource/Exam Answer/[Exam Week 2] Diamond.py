"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    loops = int(input())
    stars = 1
    space = loops
    # Top half of the diamond
    for i in range(loops):
        space -= 1
        print(" "*(space), end="")
        print("*"*stars)
        stars += 2

    # Bottom half of the diamond
    space, stars = 0, (loops*2)-3
    for i in range(loops-1):
        space += 1
        print(" "*(space), end="")
        print("*"*stars)
        stars -= 2

main()
