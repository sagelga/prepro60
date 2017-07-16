""" [Week 1] Discounted """
def main():
    """ Main function """
    cost = float(input())

    result = cost - 300
    result = max(result, 0.0)

    print(result)

main()
