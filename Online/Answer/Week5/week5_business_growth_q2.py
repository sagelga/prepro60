""" Business Growth Q2 """
def mul(num1, num2):
    """ Custom Multiply """
    if num2 == 0:
        return 0
    return num1 + mul(num1, num2 - 1)

def fac(num, cache):
    """ Factorial Function """
    if num == 1:
        cache.append(1)
        return 1
    temp = mul(cache[num - 1], num)
    cache.append(temp)
    return temp

def main():
    """ Main Function """
    num = int(input())

    cache = [1]
    for cnt in range(1, num + 1):
        print("%02d - " %cnt, "%d" %fac(cnt, cache), sep='')

main()
