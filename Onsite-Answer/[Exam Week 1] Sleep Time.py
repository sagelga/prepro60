"""
Sample Answer from P' Kumamon
This program will calculate how many hours that you have slept
"""
def main():
    """Main calculate functions"""
    sleep_time = time_to_min(int(input()), int(input()))
    wake_time = time_to_min(int(input()), int(input()))

    if sleep_time > wake_time:
        wake_time += time_to_min(24, 0)

    print("%d:%02d"%(min_to_time(wake_time - sleep_time)))

def time_to_min(hour, minuite):
    """Converts hour and minuite to the same unit : minuite"""
    minuite = minuite + (hour * 60)
    return minuite

def min_to_time(minuite):
    """Converts minuite to the normal time unit : hour and minuite"""
    hour = minuite // 60
    minuite -= (hour * 60)
    return hour, minuite

main()
