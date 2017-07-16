""" STIC """
def main():
    """ Main function """
    pat_a = "A B C D".split(' ') * 100
    pat_b = "D C B A".split(' ') * 100
    pat_c = "A A B B C C D D".split(' ') * 100
    pat_d = "A A A A B B B B C C C C D D D D".split(' ') * 50
    pat_e = "A B B A C D D C A B B A C D D C".split(' ') * 50
    result = [0, 0, 0, 0, 0]

    ans = input()
    siz_ans = len(ans)

    for cnt in enumerate(ans):
        if ans[cnt[0]] == pat_a[cnt[0]]:
            result[0] += 1
        if ans[cnt[0]] == pat_b[cnt[0]]:
            result[1] += 1
        if ans[cnt[0]] == pat_c[cnt[0]]:
            result[2] += 1
        if ans[cnt[0]] == pat_d[cnt[0]]:
            result[3] += 1
        if ans[cnt[0]] == pat_e[cnt[0]]:
            result[4] += 1

    for cnt in range(5):
        result[cnt] *= (100 / siz_ans)

    print("A: %.2f" %result[0], "%", sep='')
    print("B: %.2f" %result[1], "%", sep='')
    print("C: %.2f" %result[2], "%", sep='')
    print("D: %.2f" %result[3], "%", sep='')
    print("E: %.2f" %result[4], "%", sep='')



main()
