"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    name = input()
    total = 0

    while True:
        actions = input()

        if actions == "deposit":
            total += int(input())
        elif actions == "withdraw":
            total -= int(input())
        elif actions == "delete":
            total = 0
        else actions == "Stop":
            break

    print("%s : %d"%(name, total))
main()
