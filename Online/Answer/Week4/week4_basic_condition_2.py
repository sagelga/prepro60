""" basic condition 2 """
def main():
    """ Main function """
    score = input()
    if score.isdigit():
        score = int(score)
        if score < 0:
            print("hiwhiw")
        elif score < 50:
            print("F")
        elif score < 60:
            print("D")
        elif score < 70:
            print("C")
        elif score < 80:
            print("B")
        elif score <= 100:
            print("A")
        else:
            print("hiwhiw")
    else:
        print("hiwhiw")
main()
