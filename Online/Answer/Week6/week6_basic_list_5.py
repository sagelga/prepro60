""" Basic List 5 """
def main():
    """ Function Main """
    text = list()
    cnt = 1
    nnn = int(input())
    for _ in range(nnn):
        text += [input()]
    lng = len(text)
    for ccc in range(lng):
        print(cnt, end=' ')
        if cnt % 2 == 0:
            print("(Even)", end=' ')
        else:
            print("(Odd)", end=' ')
        print(text[ccc])
        cnt += 1

main()
