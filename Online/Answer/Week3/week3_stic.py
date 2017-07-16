""" Week 3 STIC """
def main():
    """ Main Function """
    string = input()
    cta = string.count("A")
    ctb = string.count("B")
    ctc = string.count("C")
    ctd = string.count("D")
    cte = string.count("E")
    ctt = len(string)

    print("A: %.2f" %round(cta / ctt * 100, 2), "% (", cta, "/", ctt, ")", sep='')
    print("B: %.2f" %round(ctb / ctt * 100, 2), "% (", ctb, "/", ctt, ")", sep='')
    print("C: %.2f" %round(ctc / ctt * 100, 2), "% (", ctc, "/", ctt, ")", sep='')
    print("D: %.2f" %round(ctd / ctt * 100, 2), "% (", ctd, "/", ctt, ")", sep='')
    print("E: %.2f" %round(cte / ctt * 100, 2), "% (", cte, "/", ctt, ")", sep='')

main()
