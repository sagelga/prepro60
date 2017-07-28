"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    loops, duplicates = int(input()), []
    for _ in range(loops):
        text = input().upper()
        if text not in duplicates:
            print("No")
            duplicates.append(text)
        else:
            print("Yes")

main()
