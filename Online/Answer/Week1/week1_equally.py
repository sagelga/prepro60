""" [Hardcore] [Week 1] EQUALLY Distributed """
def main():
    """ Main function """
    cost = float(input())
    each_friend = (cost / 5) // 20 * 20 # Friend pay
    friend = each_friend * 4
    kumamon = cost - friend

    print(friend)
    print(kumamon)

main()
