""" Week 4 Airport """
def main():
    """ Main function """
    choice = input()
    schdule = input()
    hour = int(schdule[0:2])
    minute = int(schdule[3:5]) + (hour * 60) + 720
    duration = schdule[5:7]

    # Check 12 system
    if hour == 12 and duration == "pm":
        duration = "am"

    # Case [A, B, C]
    if choice == "A":
        minute -= 160
    elif choice == "B":
        minute -= 140
    elif choice == "C":
        minute -= 115

    # Check remain minute
    if minute >= 720:
        minute -= 720
    elif minute < 720:
        if duration == "pm":
            duration = "am"
        elif duration == "am":
            duration = "pm"

    # Convert Minutes to hour
    hour = minute // 60
    minute -= (hour * 60)

    # Handle expert case
    if hour <= 9:
        hour = "0" + str(hour)
    if minute <= 9:
        minute = "0" + str(minute)
    if hour == "00" and duration == "pm":
        hour = "12"

    # Result
    print(str(hour), ":", str(minute), duration, sep='')

main()
