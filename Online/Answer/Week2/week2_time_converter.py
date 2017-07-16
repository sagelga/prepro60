""" Time Converter """
def main():
    """ Main Function """
    sec = int(input())
    hour = sec // 3600
    sec -= (hour * 3600)
    minute = sec // 60
    sec -= (minute * 60)

    print(str(hour) + ":" + str(minute) + ":" + str(sec))

main()
