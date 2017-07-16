""" Sum of Even or Odd """
def main():
    """ Main Function """
    choice = input()
    res = 0

    if choice == "odd":
        while 1:
            num = int(input())
            if num % 2 == 1:
                res += num
            if num == 0:
                print(res)
                break
    elif choice == "even":
        while 1:
            num = int(input())
            if num % 2 == 0:
                res += num
            if num == 0:
                print(res)
                break
    else:
        print("Error, %s" %choice, " is not even and odd.", sep='')

main()
