""" Basic List 2 """
def main():
    """ Function Main """
    text = list()
    cnt = 1
    for _ in range(5):
        text.append(input())
    for ccc in text:
        print(cnt, "-->", ccc)
        cnt += 1

main()
