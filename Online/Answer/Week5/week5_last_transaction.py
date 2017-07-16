""" Last Transaction """
def main():
    """ Main Function """
    data = []
    while 1:
        inp = input()
        try:
            if float(inp) <= 0:
                break
            else:
                data.append(float(inp))
        except (ValueError, EOFError):
            break

    res = 0
    for cnt in range(-1, -11, -1):
        try:
            res += data[cnt]
        except (IndexError, EOFError):
            break

    print("%g" %res)

main()
