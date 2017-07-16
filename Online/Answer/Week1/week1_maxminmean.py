""" Max, Mean, Min """
def main():
    """ Main function """
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())

    print("Max:", max(var1, var2, var3))
    print("Mean:", (var1 + var2 + var3) - max(var1, var2, var3) - min(var1, var2, var3))
    print("Min:", min(var1, var2, var3))

main()
