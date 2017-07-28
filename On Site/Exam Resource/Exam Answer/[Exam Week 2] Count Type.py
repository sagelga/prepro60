"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    count = [0, 0, 0]
    for i in input():
        if i.isupper():
            count[0] += 1
        if i.islower():
            count[1] += 1
        if i.isnumeric():
            count[2] += 1
    print("Upper : %d\nLower : %d\nNumber : %d"%(count[0], count[1], count[2]))
    
main()
