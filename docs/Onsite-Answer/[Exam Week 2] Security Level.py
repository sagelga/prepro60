"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    for _ in range(int(input())):
        text = input().split(" ")
        trigger = [0, 0, 0, 0]

        if len(text[1]) < 6:
            for i, _ in enumerate(trigger):
                trigger[i] = 1

        for i in text[1]:
            if i.islower():
                trigger[0] = 1
            elif i.isupper():
                trigger[1] = 1
            elif i.isnumeric():
                trigger[2] = 1
            else:
                for i, _ in enumerate(trigger):
                    trigger[i] = 1

        trigger = trigger[0] + trigger[1] + trigger[2] + trigger[3] - 1
        response = ["Low", "Medium", "High", "Invalid"]

        if not int(trigger[3]):
            print("Username: %s / Password: %s (Security-Level: %s)"%(text[0], "*" * len(text[1]), response[trigger]))
        else:
            print("Username: %s / Password: %s (%s)"%(text[0], "*" * len(text[1]), response[trigger]))


main()
