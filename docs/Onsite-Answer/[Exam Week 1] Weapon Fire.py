"""
Sample Answer from P' Kumamon
This program will count how many pew are there
"""
def main():
    """Sample answer from P' Kumamon"""
    response = input()
    fire_count = response.count("pew")

    if ((fire_count > 0) and (fire_count%2 == 0) and (fire_count < 6)) or (fire_count == 1):
        print("Semi-Automatic")
    elif fire_count > 3 or fire_count%2:
        print("Automatic")
    else:
        print("Safe")

main()
