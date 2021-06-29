"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    true_answer = input().upper()

    for i in range(1, 21):
        attempt = input().upper()

        if true_answer == attempt: # Attempt text is the right answer
            print("System Unlocked")
            break

        elif i == 20: # Attempts is over
            print("System Locked Down")

        elif len(true_answer) != len(attempt): # Attempt text is not the same length
            print("Entry Denied")

        else: # Find Likeness
            print("Likeness = %d"%(checker(true_answer, attempt)))

def checker(true_answer, attempt):
    """This is a sample answer from P' Kumamon"""
    count = 0

    for i, _ in enumerate(true_answer):
        count += (true_answer[i] == attempt[i])

    return count

main()
