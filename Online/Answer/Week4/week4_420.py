""" 4:20 """
def inp(result):
    """ input function """
    num = int(input())
    if num <= 100:
        result += num
        return result
    return result

def main():
    """ Main function """
    result = 0
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    result = inp(result)
    if result == 420:
        print("cannabis")
    else:
        print(result)

main()
